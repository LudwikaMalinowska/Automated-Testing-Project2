import unittest
from unittest.mock import Mock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_put_assert_that_response_has_status_code_200(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                            "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo)

        assert_that(response["status_code"]).is_equal_to(200)



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
