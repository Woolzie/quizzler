from models import StudyResource, StudyResourcePublic, StudyResourceGet
from sqlmodel import Session, delete
from fastapi import UploadFile
from typing import List
import uuid
from utils.file_actions import concurrently_save_file_to_disk
from core.config import settings
import asyncio

async def create_study_resources(*, session: Session, files: List[UploadFile], quiz_room_id: uuid.UUID) -> List[StudyResource]:
    """Takes a list of files for upload and returns the database records for them"""
    
    results = await asyncio.gather(*( concurrently_save_file_to_disk(f) for f in files ))
    
    resources = [
        StudyResource.model_validate(
            res,
            update={
                "url": settings.file_url_base + res.resource_id,
                "quiz_room_id": quiz_room_id
            }
            ) for res in results
    ]
    
    session.add_all(resources)
    session.commit
    
    return resources

def get_resource_path_by_id(*, session: Session, resource_id: uuid.UUID) -> StudyResourceGet:
    """Gives a StudyResourceGet model for the given resource_id"""
    
    resource = session.get(StudyResource, resource_id)
    
    if not resource:
        return None
    
    return StudyResourceGet.model_validate(resource)

def delete_resource_by_id(*, session: Session, resource_id: uuid.UUID) -> None:
    """Deletes a resource for the given ID"""
    
    delete_stmt = delete(StudyResource).where(StudyResource.resource_id == resource_id)
    session.exec(delete_stmt)
    session.commit()