#
#  Import LIBRARIES
from typing import Annotated, Any, Generator

from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm.session import Session
from starlette import status

#  Import FILES
from . import models
from .database import SessionLocal, engine
from .models import TodoRequest, Todos

#   ___


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(dependency=get_db)]


@app.get(path="/", status_code=status.HTTP_200_OK, response_model=None)
async def read_all(db: db_dependency) -> list[Any]:
    # async def read_all(db: Annotated[Session, Depends(dependency=get_db)]) -> list[Any]:
    return db.query(Todos).all()

# @app.get(path="/", status_code=status.HTTP_200_OK, response_model=None)
# async def read_all(db: db_dependency) -> list[Any]:
#     # async def read_all(db: Annotated[Session, Depends(dependency=get_db)]) -> list[Any]:
#     return db.query(Todos).all()


@app.get(path="/todo/{todo_id}", status_code=status.HTTP_200_OK, response_model=None)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)) -> Todos:
    todo_model: Todos | None = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found. ")


@app.post(path="/todo", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_todo(db: db_dependency, todo_request: TodoRequest) -> None:
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


@app.put(path="/todo", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)) -> None:
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found. ")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@app.delete(path="/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)) -> None:
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found. ")
    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()


#
#  Import LIBRARIES
#  Import FILES
#   ___
