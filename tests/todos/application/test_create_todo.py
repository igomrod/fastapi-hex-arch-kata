from unittest.mock import MagicMock, Mock

from todos.application.create_todo_service import CreateTodoService
from todos.domain.dtos import TodoCreateRequest
from todos.domain.entities import Todo


def test_should_save_todo():
    todo_create_request = TodoCreateRequest(title='A new todo',
                                            description="I am a todo")
    repository = MagicMock()
    repository.save = Mock()

    service = CreateTodoService(repository=repository)
    service.execute(todo_create_request)

    repository.save.assert_called_once_with(Todo(title='A new todo',
                                                 description="I am a todo",
                                                 days_since_created=0))
