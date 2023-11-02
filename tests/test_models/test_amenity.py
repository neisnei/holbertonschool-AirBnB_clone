#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
import models
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_name_attribute(self):
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

if __name__ == '__main__':
    unittest.main()
