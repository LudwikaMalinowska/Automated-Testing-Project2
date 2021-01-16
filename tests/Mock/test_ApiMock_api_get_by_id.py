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
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)
        first_todo = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }

        assert_that(response["data"]).is_equal_to(first_todo)

    def test_method_api_get_by_id_assert_that_response_contains_key_userId(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["data"]).contains_key("userId")

    def test_method_api_get_by_id_assert_that_response_contains_key_id(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["data"]).contains_key("id")

    def test_method_api_get_by_id_assert_that_response_contains_key_title(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["data"]).contains_key("title")

    def test_method_api_get_by_id_assert_that_response_contains_key_completed(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["data"]).contains_key("completed")

    def test_method_api_get_by_id_assert_that_response_contains_all_the_keys_userId_id_title_completed(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["data"]).contains_key("userId", "id", "title", "completed")

    def test_method_api_get_by_id_assert_that_response_has_status_code_200(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_get_all_assert_that_response_is_instance_of_dict(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"data": todos[0], "status_code": 200}
        response = self.temp.api_get_by_id(0)

        assert_that(response).is_instance_of(dict)

    def test_method_api_get_by_id_assert_that_raises_timeout_exception(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"status_code": 408}
        self.temp.api_get_by_id.side_effect = Timeout

        assert_that(self.temp.api_get_by_id).raises(Timeout).when_called_with(0)

    def test_method_api_get_by_id_assert_that_response_dont_have_status_code_200_exception(self):
        self.temp.api_get_by_id = Mock()
        self.temp.api_get_by_id.return_value = {"status_code": 408}
        response = self.temp.api_get_by_id(0)

        with self.assertRaises(Exception):
            assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_bet_by_id_assert_that_response_returns_ValueError_when_called_with_id_0_exception(self):
        self.temp.api_get_by_id = Mock()
        todo_id = 0
        self.temp.api_get_by_id.return_value = {"status_code": 408}
        self.temp.api_get_by_id.side_effect = ValueError

        assert_that(self.temp.api_get_by_id).raises(ValueError).when_called_with(todo_id)

    def test_method_api_bet_by_id_assert_that_response_returns_ValueError_when_called_with_id_300_exception(self):
        self.temp.api_get_by_id = Mock()
        todo_id = 300
        self.temp.api_get_by_id.return_value = {"status_code": 408}
        self.temp.api_get_by_id.side_effect = ValueError

        assert_that(self.temp.api_get_by_id).raises(ValueError).when_called_with(todo_id)


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()