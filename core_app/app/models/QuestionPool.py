from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

class QuestionPool(SQLModel, table=True):
    __tablename__ = "question_pools"
    
    question_pool_tag: str = Field(primary_key=True, max_length=20)
    context_collection_name: str = Field(nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: uuid.UUID = Field(foreign_key="users.user_id")
    pool_title: str
    