from models import User
from pydantic import EmailStr
from core.security import verify_password
from sqlmodel import select, Session, delete

def get_user_from_email(*, session: Session, email: EmailStr):
    select_stmt = select(User).where(User.user_email == email)
    user = session.exec(select_stmt).first()
    
    return user

def get_user_by_register_number(*, session: Session, register_number: str) -> User:
    select_stmt = select(User).where(User.user_register_no == register_number)
    db_user = session.exec(select_stmt).first()
    
    return db_user

def authenticate(*, session: Session, email: EmailStr, password: str):
    db_user = get_user_from_email(session=session, email=email)
    if not db_user:
        return None
    
    if not verify_password(password, db_user.hashed_password):
        return None
    
    return db_user

def delete_user_by_register_number(*, session: Session, register_number: str):
    """Deletes user based on given register number"""
    
    delete_stmt = delete(User).where(User.user_register_no == register_number)
    session.exec(delete_stmt)
    session.commit()
    