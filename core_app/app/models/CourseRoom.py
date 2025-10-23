from sqlmodel import Field
from models import SQLModel
import uuid

class CourseRoomBase(SQLModel):
    course_title: str = Field(nullable=False, max_length=50)
    course_sections: str = Field(max_length=50)
    course_code: str = Field(nullable=False, index=True, max_length=10)

class CourseRoom(SQLModel, table=True):
    __tablename__="course_rooms"
    
    course_room_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    course_room_code: str = Field(index=True, max_length=8)
    instructor_id: uuid.UUID = Field(foreign_key="users.user_id", nullable=False)
    is_archived: bool = Field(default=False)

class CourseRoomDetails(CourseRoomBase):
    course_room_id: uuid.UUID
    instructor_id: uuid.UUID
    instructor_name: str = Field(max_length=100)
    
class CourseRoomApi(SQLModel):
    course_room_id: uuid.UUID