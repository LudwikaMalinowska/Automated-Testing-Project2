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

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
