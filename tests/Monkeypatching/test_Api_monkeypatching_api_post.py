import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


class TestApiMonkeyPatch(unittest.TestCase):

    @patch('src.Api.Api', autospec=True)
    def test_method_api_post_raises_timeout(self, mock_class):
        mock_data = Mock()
        mock_data.return_value = {"key": "value"}
        mock_class.api_post.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_post(mock_data)

    def test_method_api_post_assert_that_called_once(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_api.api_post(mock_data)
            mock_api.api_post.assert_called_once()

    def test_method_api_post_assert_that_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_data2 = Mock()
            mock_data2.return_value = {"key2": "value2"}
            mock_api.api_post(mock_data)
            mock_api.api_post(mock_data2)
            mock_api.api_post.assert_called()

    def test_method_api_post_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_api.api_post.assert_not_called()

    def test_method_api_post_assert_that_called_with_mock_data_userId_1_title_Lorem(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post(mock_data)
            mock_api.api_post.assert_called_with(mock_data)

    def test_method_api_post_assert_that_called_once_with_mock_data_userId_1_title_Lorem(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post(mock_data)
            mock_api.api_post.assert_called_once_with(mock_data)

    def test_method_api_post_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_api.api_post(mock_data)
            with self.assertRaises(AssertionError):
                mock_api.api_post.assert_not_called()

    def test_method_api_post_assert_that_called_once_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_data2 = Mock()
            mock_data2.return_value = {"key2": "value2"}
            mock_api.api_post(mock_data)
            mock_api.api_post(mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_post.assert_called_once()

    def test_method_api_post_assert_that_called_with_mock_data_userId_1_title_Lorem_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_data2 = Mock()
            mock_data2.return_value = {
                "userId": 2,
                "title": "Lorem ipsum",
                "completed": True
            }
            mock_api.api_post(mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_post.assert_called_with(mock_data)

    def test_method_api_post_assert_that_called_once_with_mock_data_userId_1_title_Lorem_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_data2 = Mock()
            mock_data2.return_value = {
                "userId": 2,
                "title": "Lorem ipsum",
                "completed": True
            }
            mock_api.api_post(mock_data)
            mock_api.api_post(mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_post.assert_called_once_with(mock_data)

    def test_method_api_post_no_parameter_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            with self.assertRaises(TypeError):
                mock_api.api_post()


if __name__ == '__main__':
    unittest.main()
