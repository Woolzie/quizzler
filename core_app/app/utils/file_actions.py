import asyncio
import os
import uuid
from pathlib import Path
from sanitize_filename import sanitize
from core.config import settings
import aiofiles
from fastapi import UploadFile

def _safe_filename(file_name: str) -> str:
    """
    Basic sanitization: drop any path components.
    """
    secure_name = sanitize(file_name)
    
    new_file_name = secure_name.replace(" ", "_")
    new_file_name = new_file_name.replace("-", "_")
    new_file_name = new_file_name.replace(".", "")
    
    return new_file_name

async def _save_upload_to_disk(
    upload: UploadFile,
    dest_dir: Path,
    sem: asyncio.Semaphore,
    chunk_size: int,
):
    """
    Streams UploadFile to disk with a concurrency limit (via semaphores).
    Returns a dict with metadata or raises.
    Ensures upload is closed and partial file removed on error.
    """
    resource_name = _safe_filename(upload.filename or "file")
    file_id = uuid.uuid4()
    file_type = upload.filename.split(".")[1]
    file_name = file_id.hex + "." + file_type
    dest = dest_dir / file_name
    temp_dest = dest.with_suffix(dest.suffix + ".part")

    # Acquire semaphore so we limit number of concurrent writers
    async with sem:
        total = 0
        try:
            # Ensure dest_dir exists (should already be created by caller)
            async with aiofiles.open(temp_dest, "wb") as out:
                while True:
                    chunk = await upload.read(chunk_size)
                    if not chunk:
                        break
                    await out.write(chunk)
                    total += len(chunk)

            # Move temp file -> final name (atomic on same filesystem)
            os.replace(temp_dest, dest)

            return {
                "resource_id": file_id,
                "resource_name": resource_name,
                "path": dest,
                "type_of_file": file_type,
                "size": total,
                "status": "ok",
            }
        except Exception as e:
            # Clean up partial file if present
            try:
                if temp_dest.exists():
                    temp_dest.unlink()
            except Exception:
                pass
            raise e
        finally:
            # Always close the UploadFile to release temp resources
            try:
                await upload.close()
            except Exception:
                pass

async def concurrently_save_file_to_disk(f: UploadFile):
    dest_dir = Path(settings.file_upload_dir)
    concurrency = settings.file_upload_semaphore_count
    sem = asyncio.Semaphore(concurrency)
    chunk_size = settings.file_upload_chunk_size * 1024
    
    try:
        return await _save_upload_to_disk(f, dest_dir, sem, chunk_size)
    except Exception as e:
        # Return an error object instead of raising so other files continue
        return {
            "original_filename": getattr(f, "filename", None),
            "status": "error",
            "error": str(e),
        }

