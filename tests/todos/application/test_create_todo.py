from unittest.mock import MagicMock, Mock

import pytest
from pydantic import ValidationError

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


def test_should_raise_error_when_title_is_more_than_five_words():
    todo_create_request = TodoCreateRequest(title='A new todo with more than 5 words',
                                            description="I am a todo")
    repository = MagicMock()
    repository.save = Mock()

    service = CreateTodoService(repository=repository)

    with pytest.raises(ValidationError) as execinfo:
        service.execute(todo_create_request)

    assert str(execinfo.value) == '1 validation error for Todo\ntitle\n  max five words (type=value_error)'

