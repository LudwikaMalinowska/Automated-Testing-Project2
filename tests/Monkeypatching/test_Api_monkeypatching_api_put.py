import unittest

import requests
from assertpy import assert_that
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


class TestApiMonkeyPatch(unittest.TestCase):

    @patch('src.Api.Api', autospec=True)
    def test_method_api_put_raises_timeout(self, mock_class):
        mock_id = Mock()
        mock_id.return_value = 1
        mock_data = Mock()
        mock_data.return_value = {"key": "value"}
        mock_class.api_put.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_put(mock_id, mock_data)

    def test_method_api_put_assert_that_called_once(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_data = Mock()
            mock_data.return_value = {"key": "value"}
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put.assert_called_once()

    def test_method_api_put_assert_that_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
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
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put(mock_id2, mock_data2)
            mock_api.api_put.assert_called()

    def test_method_api_put_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_api.api_put.assert_not_called()

    def test_method_api_put_assert_that_called_with_id_1_and_mock_data_userId_1_title_Lorem(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put.assert_called_with(mock_id, mock_data)

    def test_method_api_put_assert_that_called_once_with_id_1_and_mock_data_userId_1_title_Lorem(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put.assert_called_once_with(mock_id, mock_data)

    def test_method_api_put_assert_that_response_has_status_code_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put.return_value = {"put_id": todo_id,
                                             "put_data": todo, "status_code": 200}
            response = mock_api.api_put(todo_id, todo)

            assert_that(response).has_status_code(200)

    def test_method_api_post_assert_that_response_status_code_is_not_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put.return_value = {"status_code": 408}
            response = mock_api.api_put(todo_id, todo)

            assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_post_assert_that_response_returns_put_data(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put.return_value = {"put_id": todo_id,
                                             "put_data": todo, "status_code": 200}
            response = mock_api.api_put(todo_id, todo)

            assert_that(response["put_data"]).is_equal_to(todo)

    def test_method_api_put_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_put(mock_id, mock_data)
            with self.assertRaises(AssertionError):
                mock_api.api_put.assert_not_called()

    def test_method_api_put_assert_that_called_once_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
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
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put(mock_id2, mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_put.assert_called_once()

    def test_method_api_put_assert_that_called_with_id_1_and_mock_data_userId_1_title_Lorem_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
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
            mock_api.api_put(mock_id2, mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_put.assert_called_with(mock_id, mock_data)

    def test_method_api_put_assert_that_called_once_with_id_1_and_mock_data_userId_1_title_Lorem_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            mock_id2 = Mock()
            mock_id2.return_value = 2
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
            mock_api.api_put(mock_id, mock_data)
            mock_api.api_put(mock_id2, mock_data2)
            with self.assertRaises(AssertionError):
                mock_api.api_put.assert_called_once_with(mock_id, mock_data)

    def test_method_api_put_no_parameter_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            with self.assertRaises(TypeError):
                mock_api.api_put()

    def test_method_api_put_only_one_parameter_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_id = Mock()
            mock_id.return_value = 1
            with self.assertRaises(TypeError):
                mock_api.api_put(mock_id)


if __name__ == '__main__':
    unittest.main()
