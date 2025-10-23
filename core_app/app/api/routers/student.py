from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from api.dependencies import SessionDep, CurrentUser
from core import config, security
from typing import Annotated
from crud import user
from models import UserPublic

student_router = APIRouter(
    prefix="/student",
    tags=["student"],
    )

@student_router.get("/me", response_model=UserPublic)
def get_me(session: SessionDep, req_student: CurrentUser):
    return req_student
