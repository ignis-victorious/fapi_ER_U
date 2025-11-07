#
#  Import LIBRARIES
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String

#  Import FILES
from .database import Base

#   ___


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


class Todos(Base):
    __tablename__: str = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
