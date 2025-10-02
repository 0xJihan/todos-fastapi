

import jwt
from fastapi import FastAPI
from pwdlib import PasswordHash

from Utils import encrypt_password, verify_password, generateToken, decodeToken
from db import mapper_registry, engine
from routers import todo
from models import *



app = FastAPI()

mapper_registry.metadata.create_all(bind=engine)

app.include_router(todo.router)


@app.get("/")
async def Test_Route():



    stmt = {
        "id":5,
        "email":"jihankhan966@gmail.com"
    }


    token = generateToken(stmt)

    decoded_token = decodeToken(token)



    return {
        "token": token,
        "decoded": decoded_token,
        "hashed_password": encrypt_password("mysecretpassword"),
        "is_verified": verify_password("mysecretpassword", encrypt_password("mysecretpassword"))
    }
