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
    create_dict = {}
    for k, v in self.__dict__.items():
      if k == "created_at" or k == "updated_at":
        # https://docs.python.org/3/library/datetime.html Stringfy Time
        create_dict[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
      else:
        if not v:
          pass
        else:
          create_dict[k] = v
    create_dict['__class__'] = self.__class.__.name__

    return create_dict
      
      


