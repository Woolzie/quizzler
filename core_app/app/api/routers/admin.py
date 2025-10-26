from models import SuccessFulResponse
from models import User, UserCreate, UserPublic, roles
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, Query, Path
from api.dependencies import CurrentAdmin, SessionDep, get_current_admin
from typing import Annotated, List
from crud import student, faculty
from utils import read_csv_files, ApiError
from sqlmodel import select, func
from pydantic import ValidationError


admin_router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)

# this one is yet to be implemented
@admin_router.post("/create_department/", dependencies=[Depends(get_current_admin)])
def create_department():
    """Takes the department detail and creates a new one in DB"""
# 

@admin_router.post("/create_student/", dependencies=[Depends(get_current_admin)], response_model=UserPublic)
def create_student(new_student: UserCreate, session: SessionDep):
    """
    Creates a single student record in the DB.
    
    Takes a UserCreate model as the body parameter
    """
    
    student_with_email = student.get_student_by_email(session=session, student_email=new_student.user_email)
    if student_with_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student with the given email already exists")
    
    created_student = student.create_new_student_in_db(session=session, new_student=new_student)
    
    return created_student

@admin_router.post("/create_students/", dependencies=[Depends(get_current_admin)])
def create_students_using_csv_file(students_file: UploadFile, session: SessionDep):
    """
    Creates students in bulk
    
    Takes a csv file and extracts students from it and registers them to the database
    """
    
    new_students = read_csv_files.get_students_from_csv(students_file.file)

    students_before_commit = session.scalar(select(func.count()).select_from(User).where(User.user_role == roles("student")))
    session.add_all(new_students)
    session.commit()
    students_after_commit = session.scalar(select(func.count()).select_from(User))
    
    if (students_after_commit - students_before_commit) <= 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong while adding new students!")
    
    return SuccessFulResponse(status_code=status.HTTP_201_CREATED, response_message="New students added to the Database")
   
@admin_router.post("/create_faculty/", dependencies=[Depends(get_current_admin)], response_model=UserPublic)
def create_faculty(new_faculty: UserCreate, session: SessionDep):
    """
    Creates a single Faculty record in the DB.
    
    Takes a UserCreate model as the body parameter
    """
    
    faculty_with_email = faculty.get_faculty_by_email(session=session, faculty_email=new_faculty.user_email)
    if faculty_with_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student with the given email already exists")
    
    created_faculty = faculty.create_new_faculty_in_db(session=session, new_faculty=new_faculty)
    
    return created_faculty

@admin_router.post("/create_faculties/", dependencies=[Depends(get_current_admin)])
def create_faculties_using_csv_file(faculties_file: UploadFile, session: SessionDep):
    """
    Creates Faculties in bulk
    
    Takes a csv file and extracts students from it and registers them to the database
    """
    
    new_faculties = read_csv_files.get_faculties_from_csv(faculties_file.file)
    
    faculties_before_commit = session.scalar(select(func.count()).select_from(User).where(User.user_role == roles("teacher")))
    session.add_all(new_faculties)
    session.commit()
    faculties_after_commit = session.scalar(select(func.count()).select_from(User).where(User.user_role == roles("teacher")))
    
    if (faculties_after_commit - faculties_before_commit) <= 0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong while adding new students!")
    
    return SuccessFulResponse(status_code=status.HTTP_201_CREATED, response_message="New Faculties added to the Database")

# yet to be implemented
@admin_router.get("/get_departments/")
def get_departments():
    return
# 

@admin_router.get("/get_faculty/", dependencies=[Depends(get_current_admin)], response_model=List[UserPublic])
def get_faculties(
    session: SessionDep,
    department_id:  Annotated[int, Query()] = None
    ):
    
    """
    Takes an optional Query Parameter:
        department_id: if given, list will be fetched department-wise
        
    This route gives you the list of faculties registered in the database
    """
    
    list_of_facutlies: List[User]
    if department_id:
        list_of_facutlies = faculty.get_facult_list_by_department_id(session=session, department_id=department_id)
    else:
        list_of_facutlies = faculty.get_faculty_list(session=session)
        
    return list_of_facutlies
 
@admin_router.get("/get_students/", dependencies=[Depends(get_current_admin)], response_model=List[UserPublic])
def get_students(
    session: SessionDep,
    department_id:  Annotated[int, Query()] = None
    ):
    
    """
    Takes an optional Query Parameter:
        department_id: if given, list will be fetched department-wise
        
    This route gives you the list of students registered in the database
    """
    
    list_of_students: List[User]
    if department_id:
        list_of_students = student.get_student_list_by_department_id(session=session, department_id=department_id)
    else:
        list_of_students = student.get_student_list(session=session)
    
    return list_of_students

# Delete student has to be changed for using id rather than register no
# register no should be a search parameter not for delete

# yet to be implemented
@admin_router.delete("delete/department/{department_id}")
def delete_department():
    return
# 

@admin_router.delete("/delete/student/{student_register_no}", dependencies=[Depends(get_current_admin)])
def delete_student(session: SessionDep, student_register_no: Annotated[str, Path(max_length=10)]):
    """Deletes Student record by using the given register number"""
    
    try:
        student.delete_student_by_register_number(session=session, register_number=student_register_no)
    except (ApiError.DatabaseException) as db_error:
        raise HTTPException(status_code=db_error.code, detail=db_error.message)
    
    return SuccessFulResponse(status_code=status.HTTP_202_ACCEPTED, response_message="Deleted the student successfully")

@admin_router.delete("/delete/faculty/{faculty_register_number}", dependencies=[Depends(get_current_admin)])
def delete_faculty(session: SessionDep, faculty_register_number: Annotated[str, Path(max_length=10)]):
    """Deletes Faculty record by using the given register number"""
    
    try:
        faculty.delete_faculty_by_register_number(session=session, register_number=faculty_register_number)
    except (ApiError.DatabaseException) as db_error:
        raise HTTPException(status_code=db_error.code, detail=db_error.message)
    
    return SuccessFulResponse(status_code=status.HTTP_202_ACCEPTED, response_message="Deleted the Faculty successfully")

# TODO: In the future, 
# add features to search faculties/students based on register number and some other attributes
# update users
# delete using triggers