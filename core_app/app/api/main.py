from fastapi import APIRouter

from api.routers import admin, login, student, course_room, quiz_room, resource

api_router = APIRouter()

api_router.include_router(admin.admin_router)
api_router.include_router(login.login_router)
api_router.include_router(student.student_router)
api_router.include_router(course_room.course_room_router)
api_router.include_router(quiz_room.quiz_room_router)
api_router.include_router(resource.resource_router)