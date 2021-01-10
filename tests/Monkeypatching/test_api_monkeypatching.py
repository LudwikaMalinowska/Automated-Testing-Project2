import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


class TestApiMonkeyPatch(unittest.TestCase):

    def test_method_api_get_all_raises_timeout(self):
        with patch('src.Api.Api') as mock_api:
            mock_api.api_get_all.side_effect = Timeout
            with self.assertRaises(Timeout):
                mock_api.api_get_all()

    @patch('src.Api.Api')
    def test_method_api_get_by_id_raises_timeout(self, mock_class):
        with patch('src.Api.Api') as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_api.api_get_by_id.side_effect = Timeout
            with self.assertRaises(Timeout):
                mock_api.api_get_by_id(mock_id)

    @patch('src.Api.Api')
    def test_method_api_post_raises_timeout(self, mock_class):
        mock_data = Mock()
        mock_data.return_value = {"key": "value"}
        mock_class.api_post.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_post(mock_data)

    @patch('src.Api.Api')
    def test_method_api_put_raises_timeout(self, mock_class):
        mock_id = Mock()
        mock_id.return_value = 1
        mock_data = Mock()
        mock_data.return_value = {"key": "value"}
        mock_class.api_put.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_put(mock_id, mock_data)

    @patch('src.Api.Api')
    def test_method_api_delete_raises_timeout(self, mock_class):
        mock_id = Mock()
        mock_id.return_value = 1
        mock_class.api_delete.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_delete(mock_id)

