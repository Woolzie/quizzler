from models import SQLModel
from sqlmodel import Field
import uuid
import datetime

# soon moving to content_generation module

# class ChatMessage(SQLModel, table=True):
#     __tablename__ = "chat_messages"
    
#     message_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
#     chat_id: uuid.UUID = Field(foreign_key="chat_history.chat_id", index=True)
#     role: str
#     content: str
#     created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)