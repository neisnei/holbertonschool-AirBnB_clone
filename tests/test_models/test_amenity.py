#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
import models
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel


import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class"""

    def test_attributes(self):
        """Test the attributes of the Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
