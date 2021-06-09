from tests.base_test import BaseAPITest
import json


class TestGETTodo(BaseAPITest):
    def test_should_return_empty_list_when_none_todo_exists(self):
        response = self._request(method="GET",
                                 endpoint="/api/todos")

        assert response.status_code == 200
        assert json.loads(response.content) == []

    def test_should_return_one_todo_when_one_todo_exists(self):
        todo = {'title': 'a new todo',
                'description': 'This is a new todo'}

        self._request(method="POST",
                      endpoint="/api/todos",
                      body=todo)

        response = self._request(method="GET",
                                 endpoint="/api/todos")

        assert response.status_code == 200
        assert json.loads(response.content) == [{'title': 'a new todo',
                                                 'description': 'This is a new todo',
                                                 'days_since_created': 0}]
