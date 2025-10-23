from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

class StudentQuestion(SQLModel, table=True):
    __tablename__ = "student_questions"
    
    assigment_id: uuid.UUID = Field(foreign_key="student_assignments.assignment_id", primary_key=True, index=True)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", primary_key=True, index=True)
    question_id: uuid.UUID = Field(foreign_key="questions.question_id", primary_key=True, index=True)
    is_answered: bool = Field(default=False)
    question_index: int
