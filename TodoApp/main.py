from typing import Annotated

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from TodoApp.db import mapper_registry, engine, get_db
from TodoApp.models import *

app = FastAPI()


mapper_registry.metadata.create_all(
    bind=engine
)

@app.get("/")
async def get_all(
        db:Annotated[Session,Depends(get_db)]
):
    return db.query(Todo).all()