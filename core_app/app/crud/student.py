from models import (User, UserCreate, UserPublic, EnrolledCourse, roles)
from sqlmodel import Session, select, and_
from core.security import get_hashed_password
from crud.user import get_user_from_email, get_user_by_register_number, delete_user_by_register_number
from typing import List
from utils import ApiError

def create_student_model(*, new_student: UserCreate) -> User:
    """
    Returns a valid User model instance to put in the db
    
    Takes UserCreate model and gives out a User model with role as student
    """
    
    student_obj = User.model_validate(
        new_student,
        update={
            "hashed_password": get_hashed_password(new_student.password),
            "user_role": roles("student")
        }
    )
    
    return student_obj

def create_new_student_in_db(*, session:Session , new_student: UserCreate) -> User:
    """
    Takes a UserCreate model and Creates a new Student in db
    """
    
    student_obj = create_student_model(new_student=new_student)
    
    session.add(student_obj)
    session.commit()
    session.refresh(student_obj)
    
    return student_obj

def get_student_by_id(*,session: Session, student_id: str) -> User:
    db_student = session.get(User, student_id)
    
    return db_student

def get_courses_enrolled_in(*, session: Session, student_id: str):
    select_stmt = select(EnrolledCourse).where(EnrolledCourse.student_id == student_id)
    courses = session.exec(select_stmt)
    
    return courses

def get_student_by_email(*, session: Session, student_email: str):
    """
    this method is a wraper around get_user_by email but doesnt add anything.
    
    its just declared here for keeping everything related to student under one module
    """
    
    student = get_user_from_email(session=session, email=student_email)
    return student

def update_student(*, session: Session):
    return

def get_student_list(*, session: Session) -> List[User]:
    select_stmt = select(User).where(User.user_role == roles("student"))
    list_of_students = session.exec(select_stmt).all()
    
    return list_of_students

def get_student_list_by_department_id(*, session:Session, department_id) -> List[User]:
    select_stmt = select(User).where(
        and_(
        User.user_role == roles("student"),
        User.department_id == department_id
    ))
    student_by_department = session.exec(select_stmt).all()
    
    return student_by_department

def delete_student_by_register_number(*, session:Session, register_number: str):
    """
    Delete a student by using their register number
    """
    
    db_student = get_user_by_register_number(session=session, register_number=register_number)
    
    if db_student.user_role != roles("student"):
        raise ApiError.DatabaseException("Given register number doesn't belong to a student!")
    
    delete_user_by_register_number(session=session, register_number=db_student.user_register_no)

    