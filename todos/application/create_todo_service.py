from todos.domain.dtos import TodoCreateRequest
from todos.domain.entities import Todo, Title, Description
from todos.infrastructure.repositories import TodoRepository


class CreateTodoService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    def execute(self, todo_create_request: TodoCreateRequest):
        todo = Todo(title=Title(value=todo_create_request.title),
                    description=Description(value=todo_create_request.description),
                    days_since_created=0)

        self._repository.save(todo)
