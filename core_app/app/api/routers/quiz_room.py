from fastapi import APIRouter, Depends, status, HTTPException
from models import SuccessFulResponse, QuizRoomCreate, QuizRoom, QuizRoomDelete, CourseRoomApi
from api.dependencies import SessionDep, get_current_faculty, get_current_user
from crud import quiz_room

quiz_room_router = APIRouter(
    prefix="/quiz_room",
    tags=["Quiz room"]
)

@quiz_room_router.post("/create", dependencies=[Depends(get_current_faculty)], response_model=QuizRoom)
def create_quiz_room(quiz_room_create: QuizRoomCreate, session: SessionDep):
    """Creates a new quiz room based on given data, Returns the newly created quiz room"""
    
    new_quiz_room = quiz_room.create_quiz_room(session=session, quiz_room_details=quiz_room_create)
    
    if not new_quiz_room:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something has gone wrong while creating the quiz room")
    
    return new_quiz_room

@quiz_room_router.get("/get-quiz-rooms", dependencies=[Depends(get_current_user)])
def get_quiz_room_by_course_id(course_room: CourseRoomApi, session: SessionDep):
    """Gets Quiz Room by using the course id"""   
    quiz_rooms = quiz_room.get_quiz_rooms_by_course_room_id(session=session, course_room=course_room)
    
    return quiz_rooms

@quiz_room_router.delete("/delete", dependencies=[Depends(get_current_faculty)])
def delete_quiz_room_by_id(quiz_room_details: QuizRoomDelete, session: SessionDep):
    """Deletes the quiz room with the given ID"""
    
    quiz_room.delete_quiz_room_by_id(session=session, quiz_room=quiz_room_details)
    
    return SuccessFulResponse(status_code=status.HTTP_202_ACCEPTED, response_message="Deleted the quiz room successfully")