import unittest

import requests
from assertpy import assert_that
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from src.Api import Api


class TestApiMonkeyPatch(unittest.TestCase):

    @patch('src.Api.Api', autospec=True)
    def test_method_api_post_raises_timeout(self, mock_class):
        mock_data = Mock()
        mock_data.return_value = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        mock_class.api_post.side_effect = Timeout
        with self.assertRaises(Timeout):
            mock_class.api_post(mock_data)

    def test_method_api_post_assert_that_called_once(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post(mock_data)
            mock_api.api_post.assert_called_once()

    def test_method_api_post_assert_that_called(self):
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
            mock_api.api_post.assert_called()

    def test_method_api_post_assert_that_not_called(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
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

    def test_method_api_post_assert_that_response_has_status_code_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post.return_value = {"posted_data": post_todo, "status_code": 200}
            response = mock_api.api_post(post_todo)
            assert_that(response).has_status_code(200)

    def test_method_api_post_assert_that_response_status_code_is_not_200(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post.return_value = {"status_code": 408}
            response = mock_api.api_post(post_todo)
            assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_post_assert_that_response_returns_posted_data(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post.return_value = {"posted_data": post_todo, "status_code": 200}
            response = mock_api.api_post(post_todo)
            assert_that(response["posted_data"]).is_equal_to(post_todo)

    def test_method_api_post_assert_that_response_is_instance_of_dict(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post.return_value = {"posted_data": post_todo, "status_code": 200}
            response = mock_api.api_post(post_todo)
            assert_that(response).is_instance_of(dict)

    def test_method_api_post_assert_that_not_called_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            mock_data = Mock()
            mock_data.return_value = {
                "userId": 1,
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post(mock_data)
            with self.assertRaises(AssertionError):
                mock_api.api_post.assert_not_called()

    def test_method_api_post_assert_that_called_once_exception(self):
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

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_empty_obj_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {}
            mock_api.api_post.return_value = {"status_code": 408}
            mock_api.api_post.side_effect = ValueError

            assert_that(mock_api.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_key_userId_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "title": "Lorem",
                "completed": False
            }
            mock_api.api_post.return_value = {"status_code": 408}
            mock_api.api_post.side_effect = ValueError

            assert_that(mock_api.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_key_title_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "completed": False
            }
            mock_api.api_post.return_value = {"status_code": 408}
            mock_api.api_post.side_effect = ValueError

            assert_that(mock_api.api_post).raises(ValueError).when_called_with(post_todo)

    def test_method_api_post_assert_that_response_returns_ValueError_when_called_with_obj_without_key_completed_exception(self):
        with patch('src.Api.Api', autospec=True) as mock_api:
            post_todo = {
                "userId": 1,
                "title": "Lorem",
            }
            mock_api.api_post.return_value = {"status_code": 408}
            mock_api.api_post.side_effect = ValueError

            assert_that(mock_api.api_post).raises(ValueError).when_called_with(post_todo)


if __name__ == '__main__':
    unittest.main()
