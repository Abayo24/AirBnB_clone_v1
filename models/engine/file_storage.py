#!/usr/bin/python3
"""File storage file"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances"""
        __file_path = 'file.json'
        __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__filepath, 'w') as file:
            sobjects = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(sobjects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                dobject = json.load(file)
                for key, value in dobjects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    obj = class_obj(**value)
                    self.__objects[key] = obj
