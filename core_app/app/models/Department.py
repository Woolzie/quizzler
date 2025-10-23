from sqlmodel import Field
from models import SQLModel

class Department(SQLModel, table=True):
    __tablename__ = "departments"
    
    department_id: int = Field(primary_key=True)
    department_name: str = Field(nullable=False, index=True, max_length=20, unique=True)