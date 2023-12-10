#!/usr/bin/python3
"""Module that defines the FileStorage Class"""
import json


class FileStorage:
    """The FileStorage Class"""
    __file_path = None
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        classname = obj.__class__.__name__
        classid = obj.id
        key = "{}.{}".format(classname, classid)
        self.__objects[key] = obj

    def save(self):
        self.__file_path = json.dumps(self.__objects)

    def reload(self):
        if self.__file_path:
            self.__objects = json.loads(self.__file_path)
