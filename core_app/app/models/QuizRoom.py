from models import SQLModel
from sqlmodel import Field
import datetime
import uuid

class QuizRoomCreate(SQLModel):
    course_room_id: uuid.UUID = Field(foreign_key="course_rooms.course_room_id", nullable=False, index=True)
    quiz_room_name: str = Field(nullable=False, index=True)
    description: str

class QuizRoom(QuizRoomCreate, table=True):
    __tablename__ = "quiz_rooms"
    
    quiz_room_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
class QuizRoomDelete(SQLModel):
    quiz_room_id: uuid.UUID
