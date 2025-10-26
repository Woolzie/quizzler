from fastapi import APIRouter, Body, Depends, Path, HTTPException, status
from api.dependencies import SessionDep, CurrentUser
from core import config, security
from typing import Annotated
from crud import user, enroll_course
from models import UserPublic, User, SuccessFulResponse
import uuid

student_router = APIRouter(
    prefix="/student",
    tags=["student"],
    )

@student_router.get("/me/", response_model=UserPublic)
def get_me(session: SessionDep, req_student: CurrentUser):
    "Just for testing"
    return req_student

@student_router.post("/enroll/")
def enroll_student(
    course_room_code: Annotated[str, Body(max_length=8)],
    session: SessionDep,
    student_info: CurrentUser):
    
    course_details = enroll_course.enroll_student_in_course(session=session,
                                                            student_id=student_info.user_id, 
                                                            course_room_code=course_room_code)
    
    if not course_details:
        return HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="No course exists with that course code")
    
    return course_details

@student_router.get("/courses/")
def get_enrolled_courses(
    session: SessionDep,
    student_info: CurrentUser
):
    courses = enroll_course.get_enrolled_courses(
        session=session,
        student_id=student_info.user_id
    )
    
    return courses

@student_router.delete("/unenroll/{course_id}")
def unenroll_student(
    course_room_id: Annotated[uuid.UUID, Path()],
    student_info: CurrentUser,
    session: SessionDep
):
    enroll_course.unenroll_student_in_course(
        session=session,
        student_id=student_info.user_id,
        course_room_id=course_room_id
    )
    
    return SuccessFulResponse(status_code=status.HTTP_204_NO_CONTENT, response_message="Unenrolled the student successfully")

