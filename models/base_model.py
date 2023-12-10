#!/usr/bin/python3
""" Module defining the base model class """
import uuid
from datetime import datetime


class BaseModel:
    """
        This is the Base Model Class for this Project
    """

    def __init__(self, *args, **kwargs):
        """initializes the instance"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Updates the 'updated_at' attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        class_name = self.__class__.__name__
        iso_created_at = self.created_at.isoformat()
        iso_updated_at = self.updated_at.isoformat()

        instance_dict = {
                "__class__": class_name,
                "id": self.id,
                "created_at": iso_created_at,
                "updated_at": iso_updated_at
        }

        return instance_dict

    def __str__(self):
        """The String representation of the BaseModel instance"""

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )
