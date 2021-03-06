import unittest
from unittest.mock import MagicMock
from assertpy import assert_that
from requests import Timeout

from src.Api import Api


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

    def test_method_api_post_assert_that_response_posted_data_contain_all_keys_userId_title_completed(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).contains_key("userId", "title", "completed")

    def test_method_api_post_assert_that_response_posted_data_has_key_userId_1(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).has_userId(1)

    def test_method_api_post_assert_that_response_posted_data_has_key_title_Lorem(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).has_title("Lorem")

    def test_method_api_post_assert_that_response_posted_data_has_key_completed_False(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response["posted_data"]).has_completed(False)

    def test_method_api_post_assert_that_response_is_instance_of_dict(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"posted_data": post_todo, "status_code": 200})
        response = self.temp.api_post(post_todo)

        assert_that(response).is_instance_of(dict)

    def test_method_api_post_assert_that_response_status_code_is_not_200(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"status_code": 408})
        response = self.temp.api_post(post_todo)

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_post_assert_that_response_returns_Timeout_exception(self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"status_code": 408}, side_effect=Timeout)

        assert_that(self.temp.api_post).raises(Timeout).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_empty_obj_exception(self):
        post_todo = {}
        self.temp.api_post = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_userId_exception(
            self):
        post_todo = {
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_title_exception(
            self):
        post_todo = {
            "userId": 1,
            "completed": False
        }
        self.temp.api_post = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_key_completed_exception(
            self):
        post_todo = {
            "userId": 1,
            "title": "Lorem",
        }
        self.temp.api_post = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(post_todo)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
