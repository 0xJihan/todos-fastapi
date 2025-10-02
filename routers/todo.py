from typing import Annotated

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.params import Depends, Path
from sqlalchemy.orm import Session
from fastapi import status
from starlette.responses import FileResponse

from db import mapper_registry, engine, get_db

from models import *

router = APIRouter()
db_dependency = Annotated[Session,Depends(get_db)]


@router.get("/todos")
async def get_all(
        db:db_dependency
):
    return db.query(Todo).all()


@router.get("/todo/{todo_id}")
async def get_todo(
        db:db_dependency,todo_id:int = Path(
            ge=0,
        )
):
    todo_model = db.get(Todo, todo_id)

    if todo_model is not None:
        return todo_model
    else:
       return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")


@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(
        db:db_dependency,
        request:TodoRequest
):
    todo_model = Todo(**request.model_dump())
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


@router.put("/todo/{todo_id}",status_code=status.HTTP_202_ACCEPTED)
async def update_todo(db:db_dependency,request:TodoRequest,todo_id:int=Path(gt=0)):


    todo_model = db.get(Todo,todo_id)

    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")

    for key,value in request.model_dump(exclude_unset=True).items():
        setattr(todo_model, key, value)

    db.commit()
    db.refresh(todo_model)
    return todo_model



@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model = db.get(Todo,todo_id)

    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")

    db.delete(todo_model)
    db.commit()
    return None