from models import SQLModel
from sqlmodel import Field
import uuid

# this model will be used in the future for adding multiple pools for one quiz
# for now, one per quiz. So only one record per quiz room

class QuizPool(SQLModel, table=True):
    __tablename__ = "quiz_pools"
    
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", primary_key=True)
    question_pool_tag: str = Field(foreign_key="question_pools.question_pool_tag", primary_key=True, max_length=20)
    