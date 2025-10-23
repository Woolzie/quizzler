from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

class StudyResource(SQLModel, table=True):
    __tablename__ = "study_resources"
    
    resource_id: uuid.UUID = Field(primary_key=True)
    resource_name: str = Field(nullable=False, max_length=100)
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", nullable=False)
    url: str = Field(nullable=False)
    path: str = Field(max_length=200)
    type_of_resource: str = Field(max_length=100)
    size: float
    uploaded_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

class StudyResourceGet(SQLModel):
    resource_name: str
    path: str

class StudyResourcePublic(SQLModel):
    resource_id: uuid.UUID
    resource_name: str
    url: str
    type_of_resource: str
