from unittest.mock import MagicMock

from tests.todos.domain.todo_builder import TodoBuilder
from todos.application.get_all_todos import GetAllTodosService


def test_should_return_all_todos():
    repository = MagicMock()

    stored_todos = [TodoBuilder().build() for _ in range(0, 2)]

    repository.get_all = MagicMock(return_value=stored_todos)

    service = GetAllTodosService(repository=repository)

    todos = service.execute()

    assert todos == stored_todos
