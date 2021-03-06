import unittest
from unittest.mock import Mock
from assertpy import assert_that
from requests import Timeout

from src.Api import Api


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

    def test_method_api_post_assert_that_response_posted_data_contain_key_userId(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).contains_key("userId")

    def test_method_api_post_assert_that_response_posted_data_contain_key_title(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).contains_key("title")

    def test_method_api_post_assert_that_response_posted_data_contain_key_completed(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).contains_key("completed")

    def test_method_api_post_assert_that_response_posted_data_contain_all_keys_userId_title_completed(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).contains_key("userId", "title", "completed")

    def test_method_api_post_assert_that_response_is_instance_of_dict(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response).is_instance_of(dict)

    def test_method_api_post_assert_that_response_posted_data_key_title_is_Lorem(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).has_title("Lorem")

    def test_method_api_post_assert_that_response_posted_data_key_userId_is_1(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).has_userId(1)

    def test_method_api_post_assert_that_response_posted_data_key_completed_is_false(self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"posted_data": todo, "status_code": 200}
        response = self.temp.api_post(todo)

        assert_that(response["posted_data"]).has_completed(False)

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

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_empty_obj_exception(self):
        self.temp.api_post = Mock()
        todo = {}
        self.temp.api_post.return_value = {"status_code": 408}
        self.temp.api_post.side_effect = ValueError

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_userId_exception(self):
        self.temp.api_post = Mock()
        todo = {
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_post.return_value = {"status_code": 408}
        self.temp.api_post.side_effect = ValueError

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_title_exception(
            self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "completed": False
        }
        self.temp.api_post.return_value = {"status_code": 408}
        self.temp.api_post.side_effect = ValueError

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_key_completed_exception(
            self):
        self.temp.api_post = Mock()
        todo = {
            "userId": 1,
            "title": "Lorem",
        }
        self.temp.api_post.return_value = {"status_code": 408}
        self.temp.api_post.side_effect = ValueError

        assert_that(self.temp.api_post).raises(ValueError).when_called_with(todo)



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()