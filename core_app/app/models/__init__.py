from sqlmodel import SQLModel

# from .ChatHistory import ChatHistory
# from .ChatMessage import ChatMessage
from .CourseRoom import CourseRoom, CourseRoomBase, CourseRoomDetails, CourseRoomApi
from .Department import Department, DepartmentCreate
from .EnrolledCourse import EnrolledCourse
from .Question import Question
from .QuestionPool import QuestionPool
from .QuizPool import QuizPool
from .QuizRoom import QuizRoom, QuizRoomCreate, QuizRoomDelete
from .StudentAnswer import StudentAnswer
from .StudentAssignment import StudentAssignment
from .StudentQuestion import StudentQuestion
from .StudyResource import StudyResource, StudyResourcePublic, StudyResourceGet
from .SuccessfulResponse import SuccessFulResponse
from .Token import TokenPayload, Token
from .User import User, UserCreate, UserPublic, roles