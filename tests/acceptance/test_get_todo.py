from tests.base_test import BaseAPITest
import json


class TestGETTodo(BaseAPITest):
    def test_should_return_empty_list_when_none_todo_exists(self):
        response = self._request(method="GET",
                                 endpoint="/api/todos")

        assert response.status_code == 200
        assert json.loads(response.content) == []
