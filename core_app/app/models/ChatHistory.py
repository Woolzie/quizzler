from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

# Soon moving to content_generation module

# class ChatHistory(SQLModel, table=True):
#     __tablename__ = "chat_history"
    
#     chat_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
#     quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", index=True)
#     chat_title: str = Field(default="New chat", max_length=100)
#     created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
#     message_id: uuid.UUID = Field(foreign_key="chat_messages.message_id")