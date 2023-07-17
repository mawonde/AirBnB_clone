#!/usr/bin/python3
"""Imports our basemodel"""
from models.base_model import BaseModel

class Review(BaseModel):
    """The review class inherits from the 
    base model class
    """
    place_id = ""
    user_id = ""
    text = ""
