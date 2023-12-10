#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import unittest


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_base_model_exists(self):
        self.assertTrue(hasattr(BaseModel, '__module__'))
        self.assertEqual(BaseModel.__name__, 'BaseModel')
        self.assertIsNotNone(BaseModel.__doc__)

    def test_base_model_attributes(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_instance_dict_exists(self):
        self.assertIsInstance(self.base_model.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
