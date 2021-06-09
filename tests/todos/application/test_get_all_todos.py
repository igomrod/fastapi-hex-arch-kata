from unittest.mock import MagicMock

from todos.application.get_all_todos import GetAllTodosService
from todos.domain.entities import Todo


def test_should_return_all_todos():
    repository = MagicMock()
    repository.get_all = MagicMock(return_value=[Todo(title='A new todo',
                                                  description="I am a todo",
                                                  days_since_created=0),
                                             Todo(title='A new todo 2',
                                                  description="I am also a todo",
                                                  days_since_created=0)
                                             ])

    service = GetAllTodosService(repository=repository)

    todos = service.execute()

    assert todos == [Todo(title='A new todo',
                          description="I am a todo",
                          days_since_created=0),
                     Todo(title='A new todo 2',
                          description="I am also a todo",
                          days_since_created=0)
                     ]
