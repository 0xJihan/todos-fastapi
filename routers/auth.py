from typing import Annotated

from click import password_option
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from database.db import get_db
from models.models import UserRequest, User
from utils.Utils import encrypt_password, generateToken, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/signup")
async def signup(
        request:UserRequest,
        db:Annotated[Session,Depends(get_db)]
):
    user_model = db.query(User).filter(User.username == request.username).first()

    if user_model is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    new_model = request.model_copy(
        update={
            "password": encrypt_password(request.password)
        }
    )
    user = User(**new_model.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    token = generateToken({
        "user_id": user.id,
        "username": user.username
    })
    return {
        "access_token": token,
        "token_type": "bearer"}


@router.post("/login")
async def login(
        db: Annotated[Session, Depends(get_db)],
        request:OAuth2PasswordRequestForm= Depends(),

):
    user_model = db.query(User).filter(User.username == request.username).first()

    if user_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(request.password, user_model.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    token = generateToken({
        "user_id": user_model.id,
        "username": user_model.username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
