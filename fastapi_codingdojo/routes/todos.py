import fastapi.responses
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel

router = APIRouter()

todos = []


class Todo(BaseModel):
    title: str
    description: str


@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo(todo: Todo):
    todos.append(todo)
    return PlainTextResponse(status_code=201, content="CREATED")


@router.get(
    "/api/todos",
    description="GET todos."
)
def get_todo():
    return JSONResponse(status_code=200, content=jsonable_encoder(todos))
