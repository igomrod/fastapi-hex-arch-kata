import dataclasses

import fastapi.responses
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel

from todos.application.create_todo_service import CreateTodoService
from todos.application.get_all_todos import GetAllTodosService
from todos.domain.dtos import TodoCreateRequest
from todos.infrastructure.repositories import TodoRepository

router = APIRouter()

todos_repository = TodoRepository()
create_todo_service = CreateTodoService(repository=todos_repository)
get_all_todo_service = GetAllTodosService(repository=todos_repository)

@router.post(
    "/api/todos",
    description="POST todo."
)
def post_todo(todo_create_request: TodoCreateRequest):
    try:
        create_todo_service.execute(todo_create_request=todo_create_request)
        return PlainTextResponse(status_code=201, content="CREATED")
    except ValueError as e:
        return PlainTextResponse(status_code=400, content=str(e))



@router.get(
    "/api/todos",
    description="GET todos."
)
def get_todo():
    todos = get_all_todo_service.execute()
    todos_dicts = [todo.dict() for todo in todos]
    return JSONResponse(status_code=200, content=todos_dicts)
