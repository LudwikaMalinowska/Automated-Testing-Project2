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

    def test_method_api_get_all_assert_that_1st_record_of_responce_equal_expected_record(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = todos
        result = self.temp.api_get_all()

        mock_first_todo = result[0]
        first_todo = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
          }
        self.assertEqual(mock_first_todo, first_todo)



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()