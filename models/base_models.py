#!/usr/bin/python3

"""
BaseModel module
Class defining all common attributes or methods of other classes
"""
from uuid import uuid4
from datetime import datetime
import models from storage

class BaseModel:
    """base class for other classes"""
    def __init__(self, *args, **kwargs):
         """__init__ method for BaseModel class
        Args:
            args (tuple): arguments
            kwargs (dict): key word arguments
        """
        dtfo = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4)
            storage.new(self)

        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(kwargs[key], dtfo)) 
                elif key != '__class__':
                     setattr(self, key, kwargs[key])

     def to_dict(self):
             """to_dict method of BaseModel creates dict with all keys/values of
        __dict__ of the instance
        Returns:
            dictionary of instance key-value pairs
        """
        dic = {"__class__": self.__class__.name__}
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

     def save(self):
        """save method of BaseModel updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
       
    def __str__(self):
        """string representation of BaseModel"""
        (self.id, self___class__.__name__, self.__dict__)

