from models import EnrolledCourse, CourseRoomDetails
from crud import course_room
from sqlmodel import Session, select
import uuid
from typing import List

def enroll_student_in_course(*, session: Session, student_id: uuid.UUID, course_room_code: str)  -> CourseRoomDetails | None:
    course_details = course_room.get_course_room_by_code(session=session, course_room_code=course_room_code)
    
    if not course_details:
        return
    
    enrollment = EnrolledCourse.model_validate(
        course_details,
        update={
            "student_id": student_id
        }
    )
    
    session.add(enrollment)
    session.commit()
    session.refresh(enrollment)
    
    return course_details

def unenroll_student_in_course(*, session: Session, student_id: uuid.UUID, course_room_id: uuid.UUID):
    course_enrolled_in = session.get(EnrolledCourse, {
        "student_id": student_id,
        "course_room_id": course_room_id
    })
    session.delete(course_enrolled_in)
    session.commit()

def get_enrolled_courses(*, session: Session, student_id: uuid.UUID) -> List[CourseRoomDetails]:
    select_stmt =  select(EnrolledCourse).where(EnrolledCourse.student_id == student_id)
    results = session.exec(select_stmt).all()
    
    courses = [course_room.get_course_room_details(
        session=session, course_room_id=res.course_room_id
    ) for res in results]
    
    return courses   