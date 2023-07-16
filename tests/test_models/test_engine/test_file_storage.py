#!/usr/bin/python3
"""Module for testing the File Storage class """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    base_model = BaseModel()

    def test_setup(self):
        """Test Settting up of the environment before each instantiation.
        Initializes the file path and clears the objects dictionary.
        """
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        FileStorage._FileStorage__objects = {}

    def test_destroy(self):
        """Test Cleaning up of the  environment after each instantiation.
        Deletes the  file.json if it exists.
        """
        if os.path.exists(self.file_path):
            # Delete the test file after the test is completed
            os.path.unlink(self.file_path)

    def test_all(self):
        """Tests the 'all' method of the FileStorage class.
        Checks if the 'all' method returns an empty dictionary.
        """
        objects = storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        """Tests the 'new' method of the FileStorage class.
        Creates a new instance and adds it to the objects dictionary.
        Checks if the object is correctly added with the expected key.
        """
        obj = TestFileStorage()
        storage.new(obj)
        objects = storage.all()
        self.assertEqual(objects, {"TestClass.1": obj})

    def test_save(self):
        """Test the 'save' a method of the FileStorage class.
        Creates a new instance, adds it to the objects dictionary, and saves it to a file.
        """
        storage = FileStorage()
        obj = TestFileStorage()
        storage.new(obj)
        storage.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Test reloading to the storage, retrieves the objects,
        and checks if the reloaded objects match the original objects.
        """
        # Reload the storage
        obj = TestFileStorage()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        reloaded_objects = reloaded_storage.all()

        self.assertEqual(reloaded_objects, {"TestFileStorage.1": obj})


if __name__ == "__main__":
    unittest.main()

