#
#  Import LIBRARIES
from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, Generator

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session

#  Import FILES
from ..database import SessionLocal
from ..models import CreateUserRequest, Token, Users

#   ___

SECRET_KEY: str = "77c7d988c2381c1607c301d798261adc633b353cf47504ef88a66937f962c1e2"
ALGORITHM: str = "HS256"

router = APIRouter(prefix="/auth", tags=["auth"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
outh2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
# outh2_bearer = OAuth2PasswordBearer(tokenUrl=" token")


def get_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(dependency=get_db)]


def authenticate_user(username: str, password: str, db: db_dependency) -> bool:
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user
    # return True


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(tz=timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def fet_current_user(token: Annotated[str, Depends(outh2_bearer)]) -> dict[str, str | int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get(" sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=" Could not validate user.")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")


#  {"username": "Manny","email": "manny@emagnu.com","first_name": "Manny","last_name": "Emagnu","password": "test12345","role": "ADMIN"}
@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=None)
# @router.post(path="/auth/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest) -> None:
    # async def create_user(db: db_dependency, create_user_request: CreateUserRequest) -> Users:
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        # hashed_password=create_user_request.password,
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()

    # return create_user_model


@router.post(path="/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency) -> str:
    # async def login_for_access_token() -> str:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=" Could not validate user.")
        # return "Failed Authentication"
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
    # return token

    # return "Successful Authentication"
    # return form_data.username
    # return "token"


# @router.get(path="/auth/")
# async def get_user() -> dict[str, str]:
#     return {"user": "authenticated"}
