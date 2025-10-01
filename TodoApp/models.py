

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean

from TodoApp.db import BASE


class Todo(BASE):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean,default=False)



class TodoRequest(BaseModel):
    title: str = Field(min_length=3,max_length=50)
    description: str = Field(min_length=3,max_length=100)
    priority: int =  Field(gt=0,lt=100)
    completed: bool