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

    def test_method_api_get_by_id_assert_that_response_contains_key_userId(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).contains_key("userId")

    def test_method_api_get_by_id_assert_that_response_contains_key_id(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).contains_key("id")

    def test_method_api_get_by_id_assert_that_response_contains_key_title(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).contains_key("title")

    def test_method_api_get_by_id_assert_that_response_contains_key_completed(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).contains_key("completed")

    def test_method_api_get_by_id_assert_that_response_contains_all_keys_userId_id_title_completed(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).contains_key("userId", "id", "title", "completed")

    def test_method_api_get_by_id_assert_that_response_has_key_userId_1(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).has_userId(1)

    def test_method_api_get_by_id_assert_that_response_has_key_id_1(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).has_id(1)

    def test_method_api_get_by_id_assert_that_response_has_key_title_delectus_aut_autem(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).has_title("delectus aut autem")

    def test_method_api_get_by_id_assert_that_response_has_key_completed_false(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response["data"]).has_completed(False)

    def test_method_api_get_by_id_assert_that_response_has_status_code_200(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"data": todos[todo_id - 1], "status_code": 200})
        response = self.temp.api_get_by_id(todo_id)

        assert_that(response).has_status_code(200)

    def test_method_api_get_by_id_assert_that_response_dont_have_status_code_200_exception(self):
        todo_id = 1
        self.temp.api_get_by_id = MagicMock(return_value={"status_code": 408})
        response = self.temp.api_get_by_id(todo_id)

        with self.assertRaises(AssertionError):
            assert_that(response).has_status_code(200)

    def test_method_api_bet_by_id_assert_that_response_returns_ValueError_when_called_with_id_0_exception(self):
        todo_id = 0
        self.temp.api_get_by_id = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_get_by_id).raises(ValueError).when_called_with(todo_id)

    def test_method_api_bet_by_id_assert_that_response_returns_ValueError_when_called_with_id_300_exception(self):
        todo_id = 300
        self.temp.api_get_by_id = MagicMock(return_value={"status_code": 408}, side_effect=ValueError)

        assert_that(self.temp.api_get_by_id).raises(ValueError).when_called_with(todo_id)

    def test_method_api_bet_by_id_assert_that_response_returns_TypeError_when_called_with_id_not_int_exception(self):
        todo_id = "1"
        self.temp.api_get_by_id = MagicMock(return_value={"status_code": 408}, side_effect=TypeError)

        assert_that(self.temp.api_get_by_id).raises(TypeError).when_called_with(todo_id)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
