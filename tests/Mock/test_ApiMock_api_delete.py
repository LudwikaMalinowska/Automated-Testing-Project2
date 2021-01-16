import unittest
from unittest.mock import Mock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_delete_assert_that_response_has_status_code_200(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_delete_assert_that_response_status_code_is_not_200(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"status_code": 408}
        response = self.temp.api_delete(todo_id)

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_delete_assert_that_response_is_instance_of_dict(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response).is_instance_of(dict)

    def test_method_api_delete_assert_that_response_has_key_delete_id_1(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response).has_delete_id(1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
