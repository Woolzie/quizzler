from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from core import config, security
from typing import Annotated
from core.db import get_session, Session
from models import User, roles
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from fastapi import HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{config.settings.api_v1_str}/login/access-token")
TokenDep = Annotated[str, Depends(oauth2_scheme)]
SessionDep = Annotated[Session, Depends(get_session)]

def get_current_user(session: SessionDep, token: TokenDep) -> User:
    try:
        decoded_token = security.get_token_payload(token)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, decoded_token.user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
CurrentUser = Annotated[User, Depends(get_current_user)]

def get_current_faculty(faculty: CurrentUser):
    if faculty.user_role != roles("teacher"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not a faculty member")
    
    return faculty
CurrentFaculty = Annotated[User, Depends(get_current_faculty)]

def get_current_admin(admin: CurrentUser):
    if admin.user_role != roles("admin"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user is not of type admin")
    
    return admin
CurrentAdmin = Annotated[User, Depends(get_current_admin)]

