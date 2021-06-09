from todos.domain.dtos import TodoCreateRequest
from todos.domain.entities import Todo
from todos.infrastructure.repositories import TodoRepository


class CreateTodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    def execute(self, todo_create_request: TodoCreateRequest):
        todo = Todo(title=todo_create_request.title,
                    description=todo_create_request.description,
                    days_since_created=0)

        self._repository.save(todo)
