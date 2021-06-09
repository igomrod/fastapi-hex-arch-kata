import fastapi.responses
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel

from todos.application.create_todo_service import CreateTodoService
from todos.domain.dtos import TodoCreateRequest
from todos.infrastructure.repositories import TodoRepository

router = APIRouter()

todos = []

create_todo_service = CreateTodoService(repository=TodoRepository)

@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo(todo_create_request: TodoCreateRequest):
    create_todo_service.execute(todo_create_request=todo_create_request)
    return PlainTextResponse(status_code=201, content="CREATED")


@router.get(
    "/api/todos",
    description="GET todos."
)
def get_todo():
    return JSONResponse(status_code=200, content=jsonable_encoder(todos))
