from sqlmodel import SQLModel

from .ChatHistory import ChatHistory
from .ChatMessage import ChatMessage
from .CourseRoom import CourseRoom, CourseRoomBase, CourseRoomDetails, CourseRoomApi
from .Department import Department
from .EnrolledCourse import EnrolledCourse
from .Question import Question
from .QuizRoom import QuizRoom, QuizRoomCreate, QuizRoomDelete
from .QuestionPool import QuestionPool
from .User import User, UserCreate, UserPublic, roles
from .StudentAnswer import StudentAnswer
from .StudentAssignment import StudentAssignment
from .StudentQuestion import StudentQuestion
from .StudyResource import StudyResource, StudyResourcePublic, StudyResourceGet
from .SuccessfulResponse import SuccessFulResponse
from .Token import TokenPayload