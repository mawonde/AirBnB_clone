#!/usr/bin/python3
"""Module for testing the Userclass  using unittest"""

import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Test the attributes & mothods of User class"""

    user = User()

    # Test if the user Model Exists
    def test_class_existance(self):
        """Test class existance"""
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_attributes(self):
        """Test if the correct attributes are created"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_data_types(self):
        """Test data types of attributes"""
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
