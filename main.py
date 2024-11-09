# main.py
from fastapi import FastAPI
from controller.user_router import  user_router
app = FastAPI()

app.include_router(router = user_router,prefix="/user")
