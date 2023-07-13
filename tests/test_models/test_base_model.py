#!/usr/bin/python3

"""our modules that we are importing, such as unittest and base model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
  """"""

  def test_str(self):
    """test if str """
    base = BaseModel()
    self.assertEqual(base.__str__(),f"[{type(base).__name__}] \ 
                    ({base.id}) {base.__dict__}")


  def test_to_dict(self):
    """"""
    base = BaseModel()
    prev_time = base.updated_at
    self.assertDictEqual(base.to_dict(),
                        {'__class__': type(base).__name__,
                        'updated_at': base.updated_at.isoformat(),
                        'id': base_id,
                        'created_at': base.created_at.isoformat()})
    base.save()
    self.assertNotEqual(prev_time, base.updated_at)


  def test_attr_classes(self):
    """"""
    base = BaseModel()
    base2 = BaseModel()
    self.assertIsInstance(base.id, str)
    self.assertIsInstance(base.created_at, datetime)
    self.assertIsInstance(base.updated_at, datetime)
    self.assertIsInstance(base.id, base2.id)



  def test_save(self):
    """"""
    base = BaseModel()
    prevtime = base.updated_at
    base.save()
    newtime = base.updated_at
    self.assertNotEqual(prevtime, newtime)
