from models.base_model import BaseModel
from datetime import datetime
import unittest


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
