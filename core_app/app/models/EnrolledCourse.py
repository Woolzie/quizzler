from sqlmodel import Field
from models import SQLModel
import uuid


class EnrolledCourse(SQLModel, table=True):
    __tablename__ = "enrolled_courses"
    
    student_id: uuid.UUID = Field(foreign_key="users.user_id", nullable=False, primary_key=True)
    course_room_id: uuid.UUID = Field(foreign_key="course_rooms.course_room_id", nullable=False, primary_key=True)