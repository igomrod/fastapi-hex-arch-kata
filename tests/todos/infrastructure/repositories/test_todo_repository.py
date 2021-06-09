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

    repository.save(Todo(title='A new todo',
                         description="I am a todo",
                         days_since_created=0))
    repository.save(Todo(title='A new todo 2',
                         description="I am a todo 2",
                         days_since_created=0))

    assert repository.get_all() == [Todo(title='A new todo',
                                         description="I am a todo",
                                         days_since_created=0),
                                    Todo(title='A new todo 2',
                                         description="I am a todo 2",
                                         days_since_created=0)]
