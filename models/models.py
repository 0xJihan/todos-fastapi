

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database.db import BASE


class Todo(BASE):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean,default=False)
    favourite = Column(Boolean,default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))



class TodoRequest(BaseModel):
    title: str = Field(min_length=3,max_length=50)
    description: str = Field(min_length=3,max_length=100)
    priority: int =  Field(gt=0,lt=100),
    favourite: bool
    completed: bool



class UserRequest(BaseModel):
    username: str = Field(min_length=3,max_length=50)
    password: str = Field(min_length=6,max_length=100)

class User(BASE):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,unique=True,index=True)
    password = Column(String)