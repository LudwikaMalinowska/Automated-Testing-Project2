import unittest
from unittest.mock import Mock, patch

from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos

class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_get_all_assert_that_result_length_equal_200(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = {"data": todos, "status_code": 200}

        result = self.temp.api_get_all()
        self.assertEqual(len(result["data"]), 200)

    def test_method_api_get_all_assert_that_result_equal_todos(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = {"data": todos, "status_code": 200}

        result = self.temp.api_get_all()
        self.assertEqual(result["data"], todos)

    def test_method_api_get_all_assert_that_1st_record_of_response_equal_expected_record(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = {"data": todos, "status_code": 200}
        result = self.temp.api_get_all()

        mock_first_todo = result["data"][0]
        first_todo = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
          }
        self.assertEqual(mock_first_todo, first_todo)

    def test_method_api_get_all_assert_that_list_of_keys_equal_to_expected_list_of_keys(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = {"data": todos, "status_code": 200}
        result = self.temp.api_get_all()

        mock_keys = list(result["data"][0].keys())
        expected_keys = ["userId", "id", "title", "completed"]

        self.assertListEqual(mock_keys, expected_keys)

    def test_method_api_get_all_assert_that_status_code_200(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = todos
        self.temp.api_get_all.status_code = 200

        self.assertEqual(self.temp.api_get_all.status_code, 200)

    def test_method_api_get_all_assert_that_side_effect_is_Timeout(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.status_code = 408
        self.temp.api_get_all.side_effect = Timeout

        self.assertEqual(self.temp.api_get_all.side_effect, Timeout)

    def test_method_api_get_all_assert_that_response_is_instance_of_dict(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.return_value = {"data": todos, "status_code": 200}
        response = self.temp.api_get_all()

        self.assertIsInstance(response, dict)

    def test_method_api_get_all_assert_that_dont_raise_timeout(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.status_code = 200
        self.temp.api_get_all.return_value = todos

        with self.assertRaises(AssertionError):
            self.assertRaises(Timeout, self.temp.api_get_all)

    def test_method_api_get_all_assert_that_raises_timeout_exception(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.status_code = 408
        self.temp.api_get_all.side_effect = Timeout

        self.assertRaises(Timeout, self.temp.api_get_all)

    def test_method_api_get_all_assert_that_wrong_status_code_exception(self):
        self.temp.api_get_all = Mock()
        self.temp.api_get_all.status_code = 408
        self.temp.api_get_all.side_effect = Timeout

        with self.assertRaises(AssertionError):
            self.assertEqual(self.temp.api_get_all.status_code, 200)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()