#!/usr/bin/python3
"""Module for testing the Stateclass  using unittest"""

import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Test the attributes & methods of state class"""

    state = State()

    # Test if the user Model Exists
    def test_class_existance(self):
        """Test State class existance"""
        cls = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state)), cls)

    def test_attributes(self):
        """Test if the correct attributes are created"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_data_types(self):
        """Test data types of attributes"""
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
