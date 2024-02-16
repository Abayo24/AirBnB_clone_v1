#!/usr/bin/python3
"""File storage file"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = f"{obj_cls_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_objs = FileStorage.__objects
        
        obj_dict = {}
        
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for key in object_dict.items():
                        cls_name, obj_id = key.split('.')
                        cls = eval(cls_name)
                        obj = cls(**object_dict)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
