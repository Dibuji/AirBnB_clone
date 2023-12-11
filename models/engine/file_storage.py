#!/usr/bin/python3
"""Module that defines the FileStorage Class"""
import json


class FileStorage:
    """The FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return the objects dict"""
        return self.__objects

    def new(self, obj):
        """creates a new obj entry in __objects"""
        classname = obj.__class__.__name__
        classid = obj.id
        key = "{}.{}".format(classname, classid)
        self.__objects[key] = obj

    def save(self):
        """Method to serialize objects to JSON"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Method to deserialize JSON"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
