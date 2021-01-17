import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock, patch
from assertpy import assert_that

from src.Api import Api
from src.todos import todos


class TestApiMonkeyPatch(unittest.TestCase):

    def test_method_api_get_all_raises_timeout(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.side_effect = Timeout
            with self.assertRaises(Timeout):
                mock_api.api_get_all()

    @patch('src.Api.Api', autospec=True)
    def test_method_api_get_all_assert_that_called_once(self, mock_class):
        mock_class.api_get_all()
        mock_class.api_get_all.assert_called_once()

    def test_method_api_get_all_assert_that_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all()
            mock_api.api_get_all()
            mock_api.api_get_all.assert_called()

    def test_method_api_get_all_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.assert_not_called()

    def test_method_api_get_all_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all()
            with self.assertRaises(AssertionError):
                mock_api.api_get_all.assert_not_called()

    def test_method_api_get_all_assert_that_called_once_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all()
            mock_api.api_get_all()
            with self.assertRaises(AssertionError):
                mock_api.api_get_all.assert_called_once()

    def test_method_api_get_all_assert_that_result_length_equal_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.return_value = {"data": todos,  "status_code": 200}
            response = mock_api.api_get_all()
            assert_that(len(response["data"])).is_equal_to(200)

    def test_method_api_get_all_assert_that_result_equal_todos(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.return_value = {"data": todos,  "status_code": 200}
            response = mock_api.api_get_all()
            assert_that(response["data"]).is_equal_to(todos)

    def test_method_api_get_all_assert_that_1st_record_of_response_equal_expected_record(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.return_value = {"data": todos,  "status_code": 200}
            response = mock_api.api_get_all()
            assert_that(response["data"][0]).is_equal_to(todos[0])

    def test_method_api_get_all_assert_that_list_of_keys_equal_to_expected_list_of_keys(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.return_value = {"data": todos,  "status_code": 200}
            response = mock_api.api_get_all()
            expected_keys = ["userId", "id", "title", "completed"]
            mock_keys = list(response["data"][0].keys())

            assert_that(mock_keys).is_equal_to(expected_keys)

    def test_method_api_get_all_assert_that_raises_Timeout(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_get_all.return_value = {"status_code": 408}
            mock_api.api_get_all.side_effect = Timeout

            assert_that(mock_api.api_get_all.side_effect).raises(Timeout)


if __name__ == '__main__':
    unittest.main()