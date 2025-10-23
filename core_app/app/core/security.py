from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Any
from datetime import timedelta, datetime
from core.config import settings
from models import TokenPayload

password_hash = PasswordHash.recommended()

def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def get_hashed_password(plain_password: str):
    return password_hash.hash(plain_password)

def create_access_token(payload: str | Any, expire_delta: timedelta) -> str:
    expire = datetime.now() + expire_delta
    to_encode = {"exp": expire, "payload": payload}
    tokenStr = jwt.encode(payload=to_encode, key=settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    
    return tokenStr

def get_token_payload(tokenStr: str) -> TokenPayload:
    # Not completed, error handling and raising has to be done
    try:
        decoded_token = jwt.decode(tokenStr, settings.jwt_secret_key, [settings.jwt_algorithm])
        token_payload = TokenPayload(**decoded_token["payload"])
        return token_payload
        
    except(InvalidTokenError):
        raise