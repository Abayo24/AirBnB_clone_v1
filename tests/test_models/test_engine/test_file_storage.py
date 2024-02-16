#!/usr/bin/python3
""""""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """tests instantiation of file storage"""
    def  test_FileStorage_instantiation_no_args(self):
        """creates file storage instance with no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """creates FileStorage instance with an arg , raises TypeError"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        """tests if var storage is an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """tests FileStorage"""
    def setUp(self):
        """creates temp test file for saving data"""
        self.test_file = "test_file.json"

    def tearDown(self):
        """removes temporary test_file after the test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        """tests if all() returns a dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """testing the new() by creating and storing an object"""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", models.storage.all())

    def test_new_with_args(self):
        """creates new obj with additional args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """creates an object with None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """tests saving objects and reloading them"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        """creates new storage instance to simulate reloading"""
        new_storage = FileStorage()
        new_storage.reload()

        """checks if reloades objs match the original objs"""
        self.assertTrue(new_storage.all().get(f"BaseModel.{obj1.id}") is not None)
        self.assertTrue(new_storage.all().get(f"BaseModel.{obj2.id}") is not None)

    def test_save_to_file(self):
        """tests saving objects to a file and check if file is created"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """tests reloading when file is empty or doesnt exist"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == "__main__":
    unittest.main()
