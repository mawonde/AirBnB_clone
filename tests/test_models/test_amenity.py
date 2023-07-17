#!/usr/bin/python3
"""Module for testing the Amenityclass  using unittest"""

import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Test the attributes & methods of Amenity class"""

    amenity = Amenity()

    # Test if the Amenity Model Exists
    def test_class_existance(self):
        """Test Amenity class existance"""
        cls = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity)), cls)

    def test_attributes(self):
        """Test if the correct attributes are created"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_data_types(self):
        """Test data types of attributes"""
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
