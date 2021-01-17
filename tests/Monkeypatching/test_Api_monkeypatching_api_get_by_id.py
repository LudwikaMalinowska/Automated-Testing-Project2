import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


class TestApiMonkeyPatch(unittest.TestCase):

    @patch('src.Api.Api', autospec=True)
    def test_method_api_get_by_id_raises_timeout(self, mock_class):
        mock_id = Mock()
        mock_id.return_value = 1
        mock_class.api_get_by_id.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_get_by_id(mock_id)

    def test_method_api_get_by_id_assert_that_called_once(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id.assert_called_once()

    def test_method_api_get_by_id_assert_that_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id(mock_id2)
            mock_api.api_get_by_id.assert_called()

    def test_method_api_get_by_id_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id.assert_not_called()

    def test_method_api_get_by_id_assert_that_called_with_id_1(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id.assert_called_with(mock_id)

    def test_method_api_get_by_id_assert_that_called_once_with_id_1(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id.assert_called_once_with(mock_id)

    def test_method_api_get_by_id_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id(mock_id)
            with self.assertRaises(AssertionError):
                mock_api.api_get_by_id.assert_not_called()

    def test_method_api_get_by_id_assert_that_called_once_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_get_by_id.assert_called_once()

    def test_method_api_get_by_id_assert_that_called_with_id_1_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_get_by_id(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_get_by_id.assert_called_with(mock_id)

    def test_api_get_by_id_monkeypatch_called_once_with_id_1_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_get_by_id(mock_id)
            mock_api.api_get_by_id(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_get_by_id.assert_called_once_with(mock_id)

    def test_method_api_get_by_id_no_parameter_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            with self.assertRaises(TypeError):
                mock_api.api_get_by_id()


if __name__ == '__main__':
    unittest.main()