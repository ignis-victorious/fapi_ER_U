#
#  Import LIBRARIES
from typing import Annotated, Any, Generator

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm.session import Session
from starlette import status

#  Import FILES
from ..database import SessionLocal
from ..models import TodoRequest, Todos

# from .routers.auth import router

#   ___


router = APIRouter()


def get_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(dependency=get_db)]


@router.get(path="/", status_code=status.HTTP_200_OK, response_model=None)
async def read_all(db: db_dependency) -> list[Any]:
    # async def read_all(db: Annotated[Session, Depends(dependency=get_db)]) -> list[Any]:
    return db.query(Todos).all()


# @router.get(path="/", status_code=status.HTTP_200_OK, response_model=None)
# async def read_all(db: db_dependency) -> list[Any]:
#     # async def read_all(db: Annotated[Session, Depends(dependency=get_db)]) -> list[Any]:
#     return db.query(Todos).all()


@router.get(path="/todo/{todo_id}", status_code=status.HTTP_200_OK, response_model=None)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)) -> Todos:
    todo_model: Todos | None = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found. ")


@router.post(path="/todo", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_todo(db: db_dependency, todo_request: TodoRequest) -> None:
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


@router.put(path="/todo", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)) -> None:
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found. ")

    # Cast the instance to Any so static type checkers don't treat attributes as Column[...] types
    todo: Any = todo_model
    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete(path="/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
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
