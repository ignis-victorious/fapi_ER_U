#
#  Import LIBRARIES
from typing import Any, Callable  # For the SessionLocal type

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

#  Import FILES
#   ___


SQLALCHEMY_DATABASE_URL: str = "sqlite:///./todos.db"

# The create_engine function returns an Engine object.
engine: Engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# The sessionmaker function returns a callable that produces Session objects.
# The type for this is a Callable which returns a Session object.
SessionLocal: Callable[..., Session] = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base() returns a base class for declarative class definitions. While it's a type object, it is often just hinted as 'Any' or, more precisely,
# 'Type[Base]' or 'object' in a simple context, but for use as a base class,
# just leaving it as is or hinting its type is common.
Base: Any = declarative_base()


#
#  Import LIBRARIES
#  Import FILES
#   ___
