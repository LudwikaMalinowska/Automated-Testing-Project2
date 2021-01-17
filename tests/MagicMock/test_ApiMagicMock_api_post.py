import unittest
from unittest.mock import Mock, MagicMock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_post_assert_that_response_has_status_code_200(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response).has_status_code(200)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
