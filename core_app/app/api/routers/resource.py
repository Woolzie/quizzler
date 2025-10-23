from fastapi import APIRouter, HTTPException, Depends, UploadFile, Query, Path, status
from fastapi.responses import FileResponse
from api.dependencies import get_current_faculty, get_current_user, SessionDep
from models import StudyResourcePublic, SuccessFulResponse
from typing import List, Annotated
from crud import study_resource
import uuid

resource_router = APIRouter(
    prefix="/resource",
    tags=["resource"]
)

@resource_router.post("/upload/", dependencies=[Depends(get_current_faculty)], response_model=List[StudyResourcePublic])
def upload_resources(resources: List[UploadFile], quiz_room_id: Annotated[uuid.UUID, Query()], session: SessionDep):
    created_resources = study_resource.create_study_resources(session=session, files=resources, quiz_room_id=quiz_room_id)
    
    return created_resources

@resource_router.get("/get/{resource_id}", dependencies=[Depends(get_current_user)])
def get_resource(resource_id: Annotated[uuid.UUID, Path()], session: SessionDep):
    resource = study_resource.get_resource_path_by_id(session=session, resource_id=resource_id)
    
    if not resource:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Wrong resource ID")
    
    return FileResponse(path=resource.path, filename=resource.resource_name)

@resource_router.delete("/delete/{resource_id}", dependencies=[Depends(get_current_faculty)])
def delete_resource(resource_id: Annotated[uuid.UUID, Path()], session: SessionDep):
    study_resource.delete_resource_by_id(session=session, resource_id=resource_id)
    
    return SuccessFulResponse(status_code=status.HTTP_204_NO_CONTENT, response_message="Resource deleted Succesfully")