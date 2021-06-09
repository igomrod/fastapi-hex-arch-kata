from faker import Faker

from tests.todos.domain.todo_builder import TodoBuilder
from todos.domain.entities import Todo
from todos.infrastructure.repositories import TodoRepository


def test_save():
    repository = TodoRepository()

    todo = Todo(title='A new todo',
                description="I am a todo",
                days_since_created=0)

    repository.save(todo)


def test_get_all_return_empty_list_when_none_todo_saved():
    repository = TodoRepository()

    assert repository.get_all() == []


def test_get_all_return_saved_todos():
    repository = TodoRepository()

    todo_1 = TodoBuilder().build()
    todo_2 = TodoBuilder().build()

    repository.save(todo_1)
    repository.save(todo_2)

    assert repository.get_all() == [todo_1, todo_2]
