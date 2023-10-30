#!/usr/bin/python3
"""Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""

import json


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object to set in __objects"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f.read())
                for key, value in objects_dict.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
