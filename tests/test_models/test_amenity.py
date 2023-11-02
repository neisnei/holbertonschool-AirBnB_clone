#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
import models
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

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
