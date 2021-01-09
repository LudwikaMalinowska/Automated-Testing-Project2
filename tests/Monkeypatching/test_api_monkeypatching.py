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
    def test_method_api_post_raises_timeout(self, mock_class):
        mock_data = Mock()
        mock_data.return_value = {"key": "value"}
        mock_class.api_post.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_post(mock_data)

