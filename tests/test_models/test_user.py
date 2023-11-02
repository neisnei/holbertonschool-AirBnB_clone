#!/usr/bin/python3

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_email_attribute(self):
        """Verify email attribute is initialized as an empty string"""
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Verify password attribute is initialized as an empty string"""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Verify first_name attribute is initialized as an empty string"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Verify last_name attribute is initialized as an empty string"""
        self.assertEqual(self.user.last_name, "")

if __name__ == '__main__':
    unittest.main()
