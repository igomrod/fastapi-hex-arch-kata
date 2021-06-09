from tests.base_test import BaseAPITest
import json


class TestPOSTTodo(BaseAPITest):
    def test_should_create_todo(self):
        todo = {'title': 'a new todo',
                'description': 'This is a new todo'}

        response = self._request(method="POST",
                                 endpoint="/api/todos",
                                 body=json.dumps(todo))

        assert response.status_code == 201
        assert response.content == b'CREATED'
