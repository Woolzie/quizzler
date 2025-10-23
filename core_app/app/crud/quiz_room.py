from models import QuizRoom, QuizRoomCreate, QuizRoomDelete, CourseRoomApi
from sqlmodel import Session, delete, select
from typing import List

def create_quiz_room(*, session: Session, quiz_room_details: QuizRoomCreate) -> QuizRoom:
    """Creates a quiz room with all the given details and returns the newly created quiz room"""
    
    quiz_room_obj = QuizRoom.model_validate(
        quiz_room_details,
    )
    
    session.add(quiz_room_obj)
    session.commit()
    session.refresh(quiz_room_obj)
    
    return quiz_room_obj

def delete_quiz_room_by_id(*, session: Session, quiz_room: QuizRoomDelete) -> None:
    """Deletes the quiz room with matching ID that is passed as an argument"""
    
    delete_stmt = delete(QuizRoom).where(QuizRoom.quiz_room_id == quiz_room.quiz_room_id)
    session.exec(delete_stmt)
    session.commit()

def get_quiz_rooms_by_course_room_id(*, session: Session, course_room: CourseRoomApi) -> List[QuizRoom] | None:
    """Gets the quiz rooms based on course room id (Ordering has to be added)"""
    select_stmt = select(QuizRoom).where(QuizRoom.course_room_id == course_room.course_room_id)
    quiz_rooms = session.exec(select_stmt).all()
    
    return quiz_rooms