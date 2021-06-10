from typing import Callable

from todos.infrastructure.repositories import TodoRepository


class GetAllTodosService:
    def __init__(self, repository: TodoRepository):
        self._repository = repository

    def execute(self):
        return self._repository.get_all()
