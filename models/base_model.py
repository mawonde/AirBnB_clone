#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
  """Defines all common attributes/methods for other classes
  """
  def __init__(self, *args, **kwargs):
    """Initializes all the class attributes"""
    



    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = self.created_at

  def __str__(self):
    """Prints the class name, id and dict as a string """
    # check if the below variables are actually strings
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
  
  def save(self):
    """Updates the a previously created object with the 
    current datetime
    """
    self.updated_at = datetime.now()

  def to_dict(self):
    """Returns a dictionary containing all keys/values
    of __dict__ of the instance
    """
  # Convert created_at and updated_at  to string object in ISO format
  # https://docs.python.org/3/tutorial/datastructures.html 5.6 Looping Tech
    disdict = dict(self.__dict__)
    disdict.update({'__class__': type(self).__name__,
                    'updated_at': self.updated_at.isoformat(),
                    'id': self.id,
                    'created_at': self.created_at.isoformat()
    return disdict
      


