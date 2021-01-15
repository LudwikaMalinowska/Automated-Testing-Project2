import unittest
from unittest.mock import Mock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos

class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_get_by_id_assert_that_response_equal_to_expected_userId_1_id_1_completed_false(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.status_code = 200
        self.temp.api_get_by_id.return_value = todos[0]
        response = self.temp.api_get_by_id(0)
        first_todo = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }

        assert_that(response).is_equal_to(first_todo)

    def test_method_api_get_by_id_assert_that_response_contains_key_userId(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = todos[0]
        response = self.temp.api_get_by_id(0)

        assert_that(response).contains_key("userId")

    def test_method_api_get_by_id_assert_that_response_contains_key_id(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = todos[0]
        response = self.temp.api_get_by_id(0)

        assert_that(response).contains_key("id")

    def test_method_api_get_by_id_assert_that_response_contains_key_title(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = todos[0]
        response = self.temp.api_get_by_id(0)

        assert_that(response).contains_key("title")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()