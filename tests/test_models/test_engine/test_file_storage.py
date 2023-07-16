#!/usr/bin/python3
"""Module for testing the File Storage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    base_model = BaseModel()

    def setUp(self):
        """Set up the environment before each test method is run."""
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the environment after each test method is run."""
        if os.path.exists(self.file_path):
            os.unlink(self.file_path)

    def test_all(self):
        """Test the 'all' method of the FileStorage class.
        Checks if the 'all' method returns an empty dictionary.
        """
        objects = storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        """Test the 'new' method of the FileStorage class.
        Creates a new instance and adds it to the objects dictionary.
        Checks if the object is correctly added with the expected key.
        """
        obj = TestFileStorage()
        storage.new(obj)
        objects = storage.all()
        self.assertEqual(objects, {"TestFileStorage.1": obj})
      
    def to_dict(self):
      """Converts the object to a dictionary."""
      return self.__dict__


    def test_save(self):
        """Test the 'save' method of the FileStorage class.
        Creates a new instance, adds it to the objects dictionary, and saves it to a file.
        """
        file_storage = FileStorage()
        obj = TestFileStorage()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists(file_storage._FileStorage__file_path))
        self.assertEqual(storage.all(), file_storage._FileStorage__objects)

    def test_reload(self):
        """Test reloading the storage, retrieves the objects,
        and checks if the reloaded objects match the original objects.
        """
        obj = TestFileStorage()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        reloaded_objects = reloaded_storage.all()
        self.assertEqual(reloaded_objects, {"TestFileStorage.1": obj})


if __name__ == "__main__":
    unittest.main()

