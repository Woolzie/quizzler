from sqlmodel import create_engine, Session
from .config import settings
from models import SQLModel

connect_args = {"check_same_thread": False}
engine = create_engine(settings.postgres_dsn)

def create_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session
