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
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response).has_status_code(200)

    def test_method_api_post_assert_that_response_returns_posted_data(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).is_equal_to(post_todo)

    def test_method_api_post_assert_that_response_returns_posted_data_doesnt_contain_key_id(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).does_not_contain_key("id")

    def test_method_api_post_assert_that_response_posted_data_contain_key_userId(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).contains_key("userId")

    def test_method_api_post_assert_that_response_posted_data_contain_key_title(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).contains_key("title")

    def test_method_api_post_assert_that_response_posted_data_contain_key_completed(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).contains_key("completed")


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
