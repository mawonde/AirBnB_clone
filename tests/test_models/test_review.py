#!/usr/bin/python3
"""Module for testing the Reviewclass  using unittest"""

import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Test the attributes & methods of Review class"""

    review = Review()

    # Test if the user Model Exists
    def test_class_existance(self):
        """Test Review class existance"""
        cls = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.review)), cls)

    def test_attributes(self):
        """Test if the correct attributes are created"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_data_types(self):
        """Test data types of attributes"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
