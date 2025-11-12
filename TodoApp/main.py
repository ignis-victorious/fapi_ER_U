#
#  Import LIBRARIES

from fastapi import FastAPI

#  Import FILES
from . import models
from .database import engine
from .routers import auth, todos

# from .routers.auth import router

#   ___


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(router=auth.router)
app.include_router(router=todos.router)
