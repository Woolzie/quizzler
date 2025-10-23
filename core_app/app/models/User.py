from models import SQLModel
from sqlmodel import Field
from pydantic import EmailStr
import uuid
import enum
from sqlalchemy import Enum
import sqlalchemy as sa
import datetime

class roles(str, enum.Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"
    
class UserBase(SQLModel):
    user_name: str = Field(max_length=100, nullable=False)
    user_register_no: str = Field(max_length=10, unique=True, nullable=False, index=True)
    # to add: date of birth
    
class UserPersonalData(UserBase):
    user_email: EmailStr = Field(unique=True, nullable=False, index=True)
    department_id: int = Field(foreign_key="departments.department_id", nullable=False)
    
class UserCreate(UserPersonalData):
    password: str = Field(min_length=8, max_length=40)
    
# the actual table in DB
class User(UserPersonalData, table=True):
    __tablename__ = "users"
    
    user_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    user_role: roles = Field(sa_column=sa.Column(Enum(roles), index=True, insert_default=roles("student")))
    hashed_password: str

class UserPublic(UserBase):
    user_id: uuid.UUID
    user_role: roles

# feature for updation of user will be introduced later:
class UserUpdate(SQLModel):
    user_name: str | None = None
    user_register_no: str | None = None
    user_email: str | None = None
    department_id: int | None = None
    
class UserPasswordUpdate(SQLModel):
    current_password: str | None = None
    new_password: str | None = None