from typing import List

from todos.domain.entities import Todo


class TodoRepository:
    def __init__(self):
        self._todos = []

    def save(self, todo: Todo):
        self._todos.append(todo)

    def get_all(self) -> List[Todo]:
        return self._todos



