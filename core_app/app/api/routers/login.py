from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from api.dependencies import SessionDep
from core import config, security
from typing import Annotated
from crud import user
from datetime import timedelta
from models import Token, TokenPayload

login_router = APIRouter(tags=["authentication/login"])

@login_router.post("/login")
def login_user(session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    valid_user = user.authenticate(session=session, email=form_data.username, password=form_data.password)
    
    if not valid_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid email or password")
    
    access_token_expiration_delta = timedelta(minutes=config.settings.access_token_expire_minutes)
    token_payload = TokenPayload(valid_user.user_id).model_dump()
        
    return Token(
        access_token = security.create_access_token(token_payload, access_token_expiration_delta)
    )