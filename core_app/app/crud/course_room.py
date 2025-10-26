from models import CourseRoomBase, CourseRoom, CourseRoomDetails, User, CourseRoomApi
from sqlmodel import Session, select, delete
import uuid
from utils import random_code_gen

def create_course_room(*, session: Session, course_base: CourseRoomBase, faculty_id: uuid.UUID) -> uuid.UUID:
    """
    Takes the creation details for a course room and gives back the created room id.
    """
    
    generated_code: str
    while True:
        generated_code = random_code_gen.gen_random_code(8)
        exists = get_course_room_by_code(generated_code)
    
        if not exists:
            break
    
    course_room_obj = CourseRoom.model_validate(
        course_base,
        update={
            "course_room_code": generated_code,
            "instructor_id": faculty_id
        }
    )
    
    session.add(course_room_obj)
    session.commit()
    session.refresh(course_room_obj)
    
    
    return course_room_obj.course_room_id

def get_course_room_details(*, session: Session, course_room_id: uuid.UUID) -> CourseRoomDetails | None:
    """Takes course_room_id and gives back the required details of the course room"""
    
    course_room = session.get(CourseRoom, course_room_id)
    
    if not course_room:
        return None
    
    faculty_incharge = session.get(User, course_room.instructor_id)
    
    if not faculty_incharge:
        return None
    
    course_room_details = CourseRoomDetails.model_validate(
        course_room,
        update={
            "intructor_name": faculty_incharge.user_name
        }
    )
    
    return course_room_details  

def get_course_room_by_code(*, session: Session, course_room_code: str) -> CourseRoomDetails | None:
    """Returns a course room based on its room_code"""
    
    select_stmt = select(CourseRoom).where(CourseRoom.course_room_code == course_room_code)
    course_room = session.exec(select_stmt).first()
    
    if not course_room:
        return None
    
    course_room_details = get_course_room_details(session=session, course_room_id=course_room.course_room_id)
    
    return course_room_details

def delete_course_room_by_id(*, session: Session, course: CourseRoomApi):
    """Deletes the course room Based on the given id
    
        Cascade Delete has to be added soon.
        
        Dependencies to be taken care of: Quiz room, Materials, Assignment...
    """
    
    delete_stmt = delete(CourseRoom).where(CourseRoom.course_room_id == course.course_room_id)
    session.exec(delete_stmt)
    session.commit()