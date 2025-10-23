from pydantic import BaseModel, Field
from models.User import roles
import uuid

class TokenPayload(BaseModel):
    user_id: uuid.UUID
    
class Token(BaseModel):
    access_token: str