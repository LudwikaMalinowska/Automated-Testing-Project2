import unittest
from unittest.mock import Mock, patch
from src.Api import Api
from tests.Mock.todos import todos

class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_get_all_assert_that_result_length_equal_200(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = todos

        result = self.temp.api_get_all()
        self.assertEqual(len(result), 200)

    def test_method_api_get_all_assert_that_result_equal_todos(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = todos

        result = self.temp.api_get_all()
        self.assertEqual(result, todos)


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()