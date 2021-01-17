import unittest
from unittest.mock import Mock, MagicMock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_put_assert_that_response_has_status_code_200(self):
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put = MagicMock(return_value={"put_data": todo, "status_code": 200})
        response = self.temp.api_put(todo_id, todo)

        assert_that(response).has_status_code(200)

    def test_method_api_put_assert_that_response_returns_put_data(self):
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put = MagicMock(return_value={"put_data": todo, "status_code": 200})
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).is_equal_to(todo)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
