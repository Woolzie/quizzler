from typing import Dict, Any
from sqlalchemy.dialects.postgresql import JSONB
from models import SQLModel
from sqlmodel import Field
import uuid
import sqlalchemy as sa

class Question(SQLModel, table=True):
    __tablename__ = "questions"
    
    question_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    mcq: Dict[str, Any] = Field(sa_column=sa.Column(JSONB))
    answer_index: int
    difficulty_level: str = Field(nullable=False)
    question_pool_tag: str = Field(nullable=False)
    question_type: str = Field(nullable=False)
    