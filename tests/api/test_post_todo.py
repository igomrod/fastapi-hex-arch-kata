from tests.base_test import BaseAPITest


class TestPOSTTodo(BaseAPITest):
    def test_should_create_todo(self):
        todo = {'title': 'a new todo',
                'description': 'This is a new todo'}

        response = self._request(method="POST",
                                 endpoint="/api/todos",
                                 body=todo)

        assert response.status_code == 201
        assert response.content == b'CREATED'

    def test_should_return_400_when_attrs_are_wrong(self):
        todo = {'title': 'this title has more than 5 words',
                'description': 'one two three four five one two three four five one two three four five WRONG'}

        response = self._request(method="POST",
                                 endpoint="/api/todos",
                                 body=todo)

        assert response.status_code == 400
        assert response.content == b'title max five words'