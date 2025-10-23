from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

class StudentAnswer(SQLModel, table=True):
    __tablename__ = "student_answers"
    
    answer_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", index=True)
    question_id: uuid.UUID = Field(foreign_key="questions.question_id", index=True)
    is_correct: bool
    answered_index: int
    answered_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)
