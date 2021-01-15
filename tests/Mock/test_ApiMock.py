import unittest
from unittest.mock import Mock, patch
from src.Api import Api

class TestApi(unittest.TestCase):

    def setUp(self):
        self.temp = Api()

    


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()