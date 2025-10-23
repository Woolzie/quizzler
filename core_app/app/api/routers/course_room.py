from fastapi import APIRouter, Depends, status
from models import CourseRoomBase, CourseRoomApi, SuccessFulResponse
from api.dependencies import CurrentFaculty, SessionDep, get_current_faculty
from crud import course_room

course_room_router = APIRouter(
    prefix="/course_room",
    tags=["Course room"]
)

@course_room_router.post("/create")
def create_course_room(course: CourseRoomBase, current_faculty: CurrentFaculty, session: SessionDep):
    """Creates a new course room based on given details"""

    course_room_id = course_room.create_course_room(session=session, course_base=course, faculty_id=current_faculty.user_id)

    return course_room_id
    
@course_room_router.delete("/delete", dependencies=[Depends(get_current_faculty)])
def delete_course_room_by_id(course_id: CourseRoomApi, session: SessionDep):
    """Deletes the course room matching with the given course_room_id"""

    delete_course_room_by_id(course_id=course_id, session=session)
    
    return SuccessFulResponse(status_code=status.HTTP_202_ACCEPTED, response_message="Deleted the course room successfully")
    
