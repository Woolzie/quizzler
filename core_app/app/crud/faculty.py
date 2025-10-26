from models import (User, UserCreate, roles, CourseRoom, CourseRoomDetails)
from sqlmodel import Session, select, and_
from core.security import get_hashed_password
from crud.user import get_user_from_email, get_user_by_register_number, delete_user_by_register_number
from typing import List
from utils import ApiError
import uuid

def create_faculty_model(*, new_faculty: UserCreate) -> User:
    """
    Returns a valid User model instance to put in the db
    
    Takes UserCreate model and gives out a User model with role as faculty
    """
    
    faculty_obj = User.model_validate(
        new_faculty,
        update={
            "hashed_password": get_hashed_password(new_faculty.password),
            "user_role": roles("teacher")
        }
    )
    
    return faculty_obj

def create_new_faculty_in_db(*, session:Session , new_faculty: UserCreate) -> User:
    """
    Takes a UserCreate model and Creates a new Faculty in db
    """
    
    student_obj = create_faculty_model(new_faculty=new_faculty)
    
    session.add(student_obj)
    session.commit()
    session.refresh(student_obj)
    
    return student_obj

def get_faculty_by_email(*, session: Session, faculty_email: str):
    """
    this method is a wraper around get_user_by email but doesnt add anything.
    
    its just declared here for keeping everything related to faculty under one module
    """
    
    student = get_user_from_email(session=session, email=faculty_email)
    return student

def get_faculty_list(*, session: Session) -> List[User]:
    select_stmt = select(User).where(User.user_role == roles("teacher"))
    list_of_faculties = session.exec(select_stmt).all()
    
    return list_of_faculties

def get_facult_list_by_department_id(*, session:Session, department_id) -> List[User]:
    select_stmt = select(User).where(
        and_(
        User.user_role == roles("teacher"),
        User.department_id == department_id
    ))
    faculties_by_department = session.exec(select_stmt).all()
    
    return faculties_by_department

def delete_faculty_by_register_number(*, session:Session, register_number: str):
    """
    Delete a faculty by using their register number
    """
    
    db_student = get_user_by_register_number(session=session, register_number=register_number)
    
    if db_student.user_role != roles("teacher"):
        raise ApiError.DatabaseException("Given register number doesn't belong to a teacher!")
    
    delete_user_by_register_number(session=session, register_number=db_student.user_register_no)

def get_faculty_courses_by_id(*, session: Session, faculty_id: uuid.UUID):
    join_stmt = select(CourseRoom, User).join(User, CourseRoom.instructor_id == User.user_id)
    print(join_stmt)
    
    results = session.exec(join_stmt).all()
    
    course_rooms = [
        CourseRoomDetails.model_validate(
            res,
            update={
                "instructor_name": res.user_name
            }
            ) for res in results
    ]
    
    return course_rooms