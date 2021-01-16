import unittest
from unittest.mock import Mock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_post_assert_that_response_has_status_code_200(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}

        response = self.temp.api_post(todo)

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_post_assert_that_response_returns_posted_data(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).is_equal_to(todo)

    def test_method_api_post_assert_that_response_returns_posted_data_doesnt_contain_key_id(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).does_not_contain_key("id")

    def test_method_api_post_assert_that_response_status_code_is_not_200_exception(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"status_code": 408}
        response = self.temp.api_post(todo)

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_post_assert_that_response_returns_Timeout_exception(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"status_code": 408}
        self.temp.api_post.side_effect = Timeout

        assert_that(self.temp.api_post).raises(Timeout).when_called_with(todo)




    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()