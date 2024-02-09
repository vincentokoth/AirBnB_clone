#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class.

    Attributes:
        id: The BaseModel id.
        created_at: The datetime at creation
        updated_at: The datetime of the last update
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *arg (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary repreentation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance"""
        d = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
