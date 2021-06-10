import datetime
from unittest.mock import MagicMock

from tests.todos.domain.todo_builder import TodoBuilder
from todos.application.get_all_todos import GetAllTodosService
from todos.domain.entities import Todo, Title, Description


def test_should_return_all_todos():
    repository = MagicMock()

    stored_todos = [TodoBuilder().build() for _ in range(0, 2)]

    repository.get_all = MagicMock(return_value=stored_todos)

    service = GetAllTodosService(repository=repository)

    todos = service.execute()

    assert todos == stored_todos


def test_should_return_proper_days_since_created():
    repository = MagicMock()

    today = MagicMock(return_value=datetime.datetime(2000, 1, 4))

    stored_todos = [Todo(title=Title(value="A new todo"),
                         description=Description(value="I am a todo created 3 days ago"),
                         created_date=datetime.datetime(2000, 1, 1),
                         _now=today)]

    repository.get_all = MagicMock(return_value=stored_todos)

    service = GetAllTodosService(repository=repository)

    todos = service.execute()

    assert todos[0].days_since_created() == 3
