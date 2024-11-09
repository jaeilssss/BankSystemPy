from fastapi import APIRouter, Body, Path

user_router = APIRouter()

@user_router.get(
    path="/{message}"
)
def hello(message: str):
    return message

@user_router.get(
    path="query"
)
def query(last_name : str, first_name : str):
    return first_name + last_name

@user_router.post(
    path="/post"
)
def test(message : str = Body()):
    return message + "입니다!"

