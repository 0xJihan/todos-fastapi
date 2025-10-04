from fastapi import FastAPI
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from routers.todo import db_dependency
from utils.Utils import encrypt_password, verify_password, generateToken, decodeToken
from database.db import mapper_registry, engine
from middleware.authenticate import authenticate_user
from routers import todo, auth

app = FastAPI()

mapper_registry.metadata.create_all(bind=engine)

app.include_router(todo.router)
app.include_router(auth.router)







