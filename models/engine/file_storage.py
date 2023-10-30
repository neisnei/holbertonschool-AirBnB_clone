#!/usr/bin/python3
"""Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object to set in __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}

        for key, obj in self.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else:'''
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
