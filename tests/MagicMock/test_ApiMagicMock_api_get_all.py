import unittest
from unittest.mock import Mock, MagicMock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_get_all_assert_that_result_length_equal_200(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        assert_that(len(response["data"])).is_equal_to(200)

    def test_method_api_get_all_assert_that_result_equal_todos(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        assert_that(response["data"]).is_equal_to(todos)

    def test_method_api_get_all_assert_that_1st_record_of_response_equal_expected_record(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        assert_that(response["data"][0]).is_equal_to(todos[0])

    def test_method_api_get_all_assert_that_list_of_keys_equal_to_expected_list_of_keys(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        expected_keys = ["userId", "id", "title", "completed"]
        mock_keys = list(response["data"][0].keys())

        self.assertListEqual(mock_keys, expected_keys)

    def test_method_api_get_all_assert_that_status_code_200(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_get_all_assert_that_status_code_is_not_200(self):
        self.temp.api_get_all = MagicMock(return_value={"status_code": 408})
        response = self.temp.api_get_all()

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_get_all_assert_that_side_effect_is_Timeout(self):
        self.temp.api_get_all = MagicMock(side_effect=Timeout)

        assert_that(self.temp.api_get_all.side_effect).is_equal_to(Timeout)

    def test_method_api_get_all_assert_that_response_is_instance_of_dict(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})
        response = self.temp.api_get_all()

        assert_that(response).is_instance_of(dict)

    def test_method_api_get_all_assert_that_dont_raise_timeout(self):
        self.temp.api_get_all = MagicMock(return_value={"data": todos, "status_code": 200})

        with self.assertRaises(AssertionError):
            self.assertRaises(Timeout, self.temp.api_get_all)

    def test_method_api_get_all_assert_that_raises_Timeout_exception(self):
        self.temp.api_get_all = MagicMock(side_effect=Timeout, return_value={"status_code": 408})

        assert_that(self.temp.api_get_all).raises(Timeout)



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
