from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

class StudentAssignment(SQLModel, table=True):
    __tablename__ = "student_assignments"
    
    assignment_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", index=True)
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", index=True)
    is_active: bool = Field(default=True)
    assigned_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)
    is_completed: bool = Field(nullable=False, default=False)
    completed_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)
    score: float = Field(default=0) 