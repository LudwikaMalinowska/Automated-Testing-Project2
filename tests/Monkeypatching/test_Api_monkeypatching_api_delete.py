import unittest

import requests
from assertpy import assert_that
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api
from src.todos import todos


class TestApiMonkeyPatch(unittest.TestCase):

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
    
    def test_method_api_delete_assert_that_response_has_status_code_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"delete_id": todo_id,
                                                "deleted_data": todos[todo_id - 1],
                                                "status_code": 200}
            response = mock_api.api_delete(todo_id)
    
            assert_that(response).has_status_code(200)
    
    def test_method_api_delete_assert_that_response_status_code_is_not_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"status_code": 408}
            response = mock_api.api_delete(todo_id)
    
            assert_that(response["status_code"]).is_not_equal_to(200)
    
    def test_method_api_delete_assert_that_response_is_instance_of_dict(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"delete_id": todo_id,
                                                "deleted_data": todos[todo_id - 1],
                                                "status_code": 200}
            response = mock_api.api_delete(todo_id)
    
            assert_that(response).is_instance_of(dict)
    
    def test_method_api_delete_assert_that_response_has_key_delete_id_1(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"delete_id": todo_id,
                                                "deleted_data": todos[todo_id - 1],
                                                "status_code": 200}
            response = mock_api.api_delete(todo_id)

            assert_that(response).has_delete_id(1)
    
    def test_method_api_delete_assert_that_response_returns_deleted_data(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"delete_id": todo_id,
                                                "deleted_data": todos[todo_id - 1],
                                                "status_code": 200}
            response = mock_api.api_delete(todo_id)
    
            assert_that(response["deleted_data"]).is_equal_to(todos[0])
    
    def test_method_api_delete_assert_that_response_deleted_data_contain_all_keys_userId_id_title_completed(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            todo_id = 1
            mock_api.api_delete.return_value = {"delete_id": todo_id,
                                                "deleted_data": todos[todo_id - 1],
                                                "status_code": 200}
            response = mock_api.api_delete(todo_id)
    
            assert_that(response["deleted_data"]).contains_key("userId", "id", "title", "completed")

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