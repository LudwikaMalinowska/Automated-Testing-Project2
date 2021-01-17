import unittest
from unittest.mock import Mock, MagicMock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_get_by_id_assert_that_response_equal_to_expected_userId_1_id_1_completed_false(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)
        expected_todo = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
          }

        assert_that(response["data"]).is_equal_to(expected_todo)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
