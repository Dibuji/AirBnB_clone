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
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Method to deserialize JSON"""
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                class_obj = {'BaseModel': BaseModel}.get(class_name)
                if class_obj:
                    instance = class_obj(**obj_dict)
                    self.__objects[key] = instance

        except FileNotFoundError:
            pass
