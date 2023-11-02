#!/usr/bin/python3

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_state_id_attribute(self):
        """Verify that the state_id attribute is initialized as an empty string"""
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """Verify that the name attribute is initialized as an empty string"""
        self.assertEqual(self.city.name, "")

    def test_state_id_assignment(self):
        """Verify that a new value can be assigned to the state_id attribute"""
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_name_assignment(self):
        """Verify that a new value can be assigned to the name attribute"""
        self.city.name = "Los Angeles"
        self.assertEqual(self.city.name, "Los Angeles")

if __name__ == '__main__':
    unittest.main()
