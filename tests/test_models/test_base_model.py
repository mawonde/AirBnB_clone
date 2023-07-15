#!/usr/bin/python3
"""Module for testing the parent class i.e BaseModel using unittest"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests the attributes and methods of the BaseModel"""

    base_model = BaseModel()

    def test_init(self):
        """Tests the __init__ attributes and their values
        of the BaseModel
        """
        # Derive our tests according to the exploratory testing above
        self.base_model.name = "My First Model"  # set the name attribute
        self.base_model.my_number = 20  # set the number attribute
        self.base_model.save()  # call the save method
        base_model_json = (
            self.base_model.to_dict()
        )  # conversion of the base model to a dict

        self.assertEqual(self.base_model.name, base_model_json["name"], "Pass")
        self.assertEqual(
            self.base_model.my_number, base_model_json["my_number"], "Pass"
        )
        self.assertEqual("BaseModel", base_model_json["__class__"], "Pass")
        self.assertEqual(self.base_model.id, base_model_json["id"], "Pass")

    def test_str(self):
        """Tests the output string"""
        expected_output = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__
        )
        self.assertEqual(str(self.base_model), expected_output, "Pass")

    def test_save(self):
        """Tests the time diff between  updating of an object"""
        prev_time = self.base_model.updated_at
        self.base_model.save()
        new_time = self.base_model.updated_at
        self.assertNotEqual(prev_time, new_time, "Pass")
        # On Creation check if the created time is equal to the updated time
        self.assertIsInstance(self.base_model.created_at, datetime, "Pass")
        self.assertIsInstance(self.base_model.updated_at, datetime, "Pass")

    def test_to_dict(self):
        """Tests the keys of a dictionary"""
        
        base_model_json = self.base_model.to_dict()
        self.assertIn("id", base_model_json)
        self.assertIn("created_at", base_model_json)
        self.assertIn("updated_at", base_model_json)
        self.assertIn("__class__", base_model_json)


if __name__ == '__main__':
    unittest.main()
