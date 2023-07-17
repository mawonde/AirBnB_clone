#!/usr/bin/python3
"""Module for testing the Cityclass  using unittest"""

import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Test the attributes & methods of City class"""

    city = City()

    # Test if the user Model Exists
    def test_class_existance(self):
        """Test City class existance"""
        cls = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.city)), cls)

    def test_attributes(self):
        """Test if the correct attributes are created"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_data_types(self):
        """Test data types of attributes"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
