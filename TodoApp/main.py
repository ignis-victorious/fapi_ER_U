#
#  Import LIBRARIES
#  Import FILES
# from .models import Todos
from fastapi import FastAPI

from . import models
from .database import engine

#   ___


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
