from fastapi import FastAPI

from app.controllers.UserController import router

app = FastAPI()

app.include_router(router)