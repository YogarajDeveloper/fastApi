from fastapi import FastAPI

from app.database import engine, Base
from app.controllers.UserController import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)