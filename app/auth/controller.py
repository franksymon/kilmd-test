from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, Any
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta






# Services
from app.auth.service import authenticate

# Config
from config.config import settings
from app.core.security import create_access_token, CurrentUser, SessionDep

# Schemas
from app.auth.schema import Token

router = APIRouter(tags=["auth"], prefix="/login")


@router.post("/signup")
async def signup():
    ...

@router.post("/access-token")
def login_access_token(db: SessionDep,  form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    
    user = authenticate(db=db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inactive user")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(access_token=create_access_token(user, expires_delta=access_token_expires))

