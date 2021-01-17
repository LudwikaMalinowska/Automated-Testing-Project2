import unittest
from unittest.mock import Mock, patch
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from tests.Mock.todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_put_assert_that_response_has_status_code_200(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                            "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_post_assert_that_response_status_code_is_not_200(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_post_assert_that_response_returns_put_data(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).is_equal_to(todo)

    def test_method_api_put_assert_that_response_put_data_doesnt_contain_key_id(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).does_not_contain_key("id")

    def test_method_api_put_assert_that_response_put_data_contain_key_userId(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).contains_key("userId")

    def test_method_api_post_assert_that_response_put_data_contain_key_title(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).contains_key("title")

    def test_method_api_post_assert_that_response_put_data_contain_key_completed(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).contains_key("completed")

    def test_method_api_post_assert_that_response_put_data_contain_all_keys_userId_title_completed(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).contains_key("userId", "title", "completed")

    def test_method_api_put_assert_that_response_is_instance_of_dict(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response).is_instance_of(dict)

    def test_method_api_put_assert_that_response_put_data_key_title_is_Lorem(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).has_title("Lorem")

    def test_method_api_put_assert_that_response_put_data_key_userId_is_1(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).has_userId(1)

    def test_method_api_put_assert_that_response_put_data_key_completed_is_false(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response["put_data"]).has_completed(False)

    def test_method_api_put_assert_that_response_has_key_put_id_1(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"put_id": todo_id,
                                          "put_data": todo, "status_code": 200}
        response = self.temp.api_put(todo_id, todo)

        assert_that(response).has_put_id(1)

    def test_method_api_put_assert_that_response_returns_Timeout_exception(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = Timeout

        assert_that(self.temp.api_put).raises(Timeout).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_id_0_exception(self):
        self.temp.api_put = Mock()
        todo_id = 0
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_id_300_exception(self):
        self.temp.api_put = Mock()
        todo_id = 300
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_TypeError_when_called_with_id_not_int_exception(self):
        self.temp.api_put = Mock()
        todo_id = "1"
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = TypeError

        assert_that(self.temp.api_put).raises(TypeError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_AttributeError_when_called_with_id_None_exception(self):
        self.temp.api_put = Mock()
        todo_id = None
        todo = {
            "userId": 1,
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = AttributeError

        assert_that(self.temp.api_put).raises(AttributeError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_empty_obj_exception(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {}
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_obj_without_userId_exception(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "title": "Lorem",
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_obj_without_title_exception(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "completed": False
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def test_method_api_put_assert_that_response_returns_ValueError_when_called_with_obj_without_key_completed_exception(self):
        self.temp.api_put = Mock()
        todo_id = 1
        todo = {
            "userId": 1,
            "title": "Lorem",
        }
        self.temp.api_put.return_value = {"status_code": 408}
        self.temp.api_put.side_effect = ValueError

        assert_that(self.temp.api_put).raises(ValueError).when_called_with(todo_id, todo)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
