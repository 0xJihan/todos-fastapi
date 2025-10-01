from sqlalchemy import Column, Integer, String, Boolean

from TodoApp.db import BASE


class Todo(BASE):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean,default=False)