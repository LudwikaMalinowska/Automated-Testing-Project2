import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


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







##### DELETE
    @patch('src.Api.Api', autospec=True)
    def test_method_api_delete_raises_timeout(self, mock_class):
        mock_id = Mock()
        mock_id.return_value = 1
        mock_class.api_delete.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_delete(mock_id)

    def test_method_api_delete_assert_that_called_once(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_delete(mock_id)
            mock_api.api_delete.assert_called_once()

    def test_method_api_delete_assert_that_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_delete(mock_id)
            mock_api.api_delete(mock_id2)
            mock_api.api_delete.assert_called()

    def test_method_api_delete_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_delete.assert_not_called()

    def test_method_api_delete_assert_that_called_with_id_1(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_delete(mock_id)
            mock_api.api_delete.assert_called_with(mock_id)

    def test_method_api_delete_assert_that_called_once_with_id_1(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_delete(mock_id)
            mock_api.api_delete.assert_called_once_with(mock_id)

    def test_method_api_delete_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_delete(mock_id)
            with self.assertRaises(AssertionError):
                mock_api.api_delete.assert_not_called()

    def test_method_api_delete_assert_that_called_once_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_delete(mock_id)
            mock_api.api_delete(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_delete.assert_called_once()

    def test_method_api_delete_assert_that_called_with_id_1_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_delete(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_delete.assert_called_with(mock_id)

    def test_method_api_delete_assert_that_called_once_with_id_1_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
            mock_api.api_delete(mock_id)
            mock_api.api_delete(mock_id2)
            with self.assertRaises(AssertionError):
                mock_api.api_delete.assert_called_once_with(mock_id)

    def test_method_api_delete_no_parameter_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            with self.assertRaises(TypeError):
                mock_api.api_delete()



if __name__ == '__main__':
    unittest.main()