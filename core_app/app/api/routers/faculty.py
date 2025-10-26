from models import User, CourseRoomDetails
from api.dependencies import get_current_faculty, CurrentFaculty, SessionDep
from fastapi import APIRouter, Depends
from crud import faculty

faculty_router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)

@faculty_router.get("/courses")
def get_course_rooms(faculty_details: CurrentFaculty, session: SessionDep):
    course_rooms = faculty.get_faculty_courses_by_id(session=session, faculty_id=faculty_details.user_id)
    return course_rooms