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
    days_since_created: int


class TodoPostRequest(BaseModel):
    title: str
    description: str


@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo(todo: TodoPostRequest):
    todos.append(Todo(title=todo.title, description=todo.description, days_since_created=0))
    return PlainTextResponse(status_code=201, content="CREATED")


@router.get(
    "/api/todos",
    description="GET todos."
)
def get_todo():
    return JSONResponse(status_code=200, content=jsonable_encoder(todos))
