import unittest
from unittest.mock import Mock
from assertpy import assert_that
from requests import Timeout

from src.Api import Api
from todos import todos


class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    def test_method_api_delete_assert_that_response_has_status_code_200(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["status_code"]).is_equal_to(200)

    def test_method_api_delete_assert_that_response_status_code_is_not_200(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"status_code": 408}
        response = self.temp.api_delete(todo_id)

        assert_that(response["status_code"]).is_not_equal_to(200)

    def test_method_api_delete_assert_that_response_is_instance_of_dict(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response).is_instance_of(dict)

    def test_method_api_delete_assert_that_response_has_key_delete_id_1(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response).has_delete_id(1)

    def test_method_api_delete_assert_that_response_returns_deleted_data(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).is_equal_to(todos[0])

    def test_method_api_delete_assert_that_response_deleted_data_contain_key_userId(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).contains_key("userId")

    def test_method_api_delete_assert_that_response_deleted_data_contain_key_id(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).contains_key("id")

    def test_method_api_delete_assert_that_response_deleted_data_contain_key_title(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).contains_key("title")

    def test_method_api_delete_assert_that_response_deleted_data_contain_key_completed(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).contains_key("completed")

    def test_method_api_delete_assert_that_response_deleted_data_contain_all_keys_userId_id_title_completed(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).contains_key("userId", "id", "title", "completed")

    def test_method_api_delete_assert_that_response_deleted_data_has_key_userId_1(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).has_userId(1)

    def test_method_api_delete_assert_that_response_deleted_data_has_key_id_1(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).has_id(1)

    def test_method_api_delete_assert_that_response_deleted_data_has_key_title_delectus_aut_autem(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).has_title("delectus aut autem")

    def test_method_api_delete_assert_that_response_deleted_data_has_key_completed_False(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"delete_id": todo_id,
                                             "deleted_data": todos[todo_id - 1],
                                             "status_code": 200}
        response = self.temp.api_delete(todo_id)

        assert_that(response["deleted_data"]).has_completed(False)

    def test_method_api_delete_assert_that_response_returns_Timeout_exception(self):
        self.temp.api_delete = Mock()
        todo_id = 1
        self.temp.api_delete.return_value = {"status_code": 408}
        self.temp.api_delete.side_effect = Timeout

        assert_that(self.temp.api_delete).raises(Timeout).when_called_with(todo_id)

    def test_method_api_delete_assert_that_response_returns_ValueError_when_called_with_id_0_exception(self):
        self.temp.api_delete = Mock()
        todo_id = 0
        self.temp.api_delete.return_value = {"status_code": 408}
        self.temp.api_delete.side_effect = ValueError

        assert_that(self.temp.api_delete).raises(ValueError).when_called_with(todo_id)

    def test_method_api_delete_assert_that_response_returns_ValueError_when_called_with_id_300_exception(self):
        self.temp.api_delete = Mock()
        todo_id = 300
        self.temp.api_delete.return_value = {"status_code": 408}
        self.temp.api_delete.side_effect = ValueError

        assert_that(self.temp.api_delete).raises(ValueError).when_called_with(todo_id)

    def test_method_api_delete_assert_that_response_returns_TypeError_when_called_with_id_not_int_exception(self):
        self.temp.api_delete = Mock()
        todo_id = "1"
        self.temp.api_delete.return_value = {"status_code": 408}
        self.temp.api_delete.side_effect = TypeError

        assert_that(self.temp.api_delete).raises(TypeError).when_called_with(todo_id)

    def test_method_api_delete_assert_that_response_returns_AttributeError_when_called_with_None_exception(self):
        self.temp.api_delete = Mock()
        todo_id = None
        self.temp.api_delete.return_value = {"status_code": 408}
        self.temp.api_delete.side_effect = AttributeError

        assert_that(self.temp.api_delete).raises(AttributeError).when_called_with(todo_id)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
