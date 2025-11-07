#
#  Import LIBRARIES
#  Import FILES
from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

#   ___


class Todos(Base):
    __tablename__: str = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
