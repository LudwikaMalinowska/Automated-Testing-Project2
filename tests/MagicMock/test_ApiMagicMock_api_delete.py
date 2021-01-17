import unittest
from unittest.mock import Mock, MagicMock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_delete_assert_that_response_has_status_code_200(self):
        todo_id = 1
        self.temp.api_delete = MagicMock(return_value={"delete_id": todo_id, "deleted_data": todos[todo_id - 1],
                                                       "status_code": 200})
        response = self.temp.api_delete(todo_id)

        assert_that(response).has_status_code(200)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
