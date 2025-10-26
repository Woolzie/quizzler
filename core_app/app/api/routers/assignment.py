from fastapi import APIRouter
from models import StudentAssignment, StudentAnswer, StudentQuestion

student_assignment_router = APIRouter(
    prefix="/assignment",
    tags=["assignment"]
)

# All of these are yet to be implemented:

@student_assignment_router.post("/create-from-pool")
def create_assignment_from_pool():
    """This route will take the pool tag and assign questions to students. this is the Algorithm Part"""
    
    return

@student_assignment_router.post("/create-from-material")
def create_pool_from_material():
    """
    This route deals with the material and content_gen apis to create new question pool
    
    It needs to automatically create new assigment once pool is created
    """
    return

@student_assignment_router.delete("/delete-assignment")
def delete_assingment():
    """this route is supposed to delete the assignment using quiz_room_id and student_id"""
    return

@student_assignment_router.post("/submit-answer")
def submit_answer():
    """Takes the answer to an assignment question and hands it in"""
    
@student_assignment_router.get("/questions")
def get_assignment_questions():
    "Returns the assignment assigned to the student"
    
@student_assignment_router.put("/update-assignment")
def update_assignment_deadline():
    """Updates the assignment deadline"""