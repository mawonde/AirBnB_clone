#!/usr/bin/python3
"""Class to defines all common attributes/methods"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes all the class attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(kwargs[k], fmt)
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Prints the class name, id and dict as a string"""
        # check if the below variables are actually strings
        cls = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return "[{}] ({}) {}".format(cls, id, dict)

    def save(self):
        """Updates the a previously created object with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        # Convert created_at and updated_at  to string object in ISO format
        # by making a new dict from the self.dict
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
