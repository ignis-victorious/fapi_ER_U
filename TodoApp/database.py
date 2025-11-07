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


# INSERT INTO todos (title, description, priority, complete) VALUES ('Go to store', 'To pick up eggs', 4, False);

# INSERT INTO todos (title, description, priority, complete) VALUES ('Cut the loan', 'Grass is getting longer', 3, False);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Feed dog', 'He is getting hungry', 5, 0);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Test element', 'He is getting hungry', 5, 0);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Haircut', 'Need to get length 1mm', 3, False);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Feed dog', 'Make sure to use new food brand' 5, 0)
# INSERT INTO todos (title, description, priority, complete) VALUES ('Water plant', 'Inside and Outside plants', 4, False);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Learn somethng new', 'Learn to code', 5, False);
# INSERT INTO todos (title, description, priority, complete) VALUES ('Shower', 'You have not showered on months', 5, False);

#  Import LIBRARIES
#  Import FILES
#   ___
