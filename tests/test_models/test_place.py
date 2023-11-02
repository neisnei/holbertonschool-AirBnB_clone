#!/usr/bin/python3

import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_city_id_attribute(self):
        """Verify that the city_id attribute is initialized as an empty string"""
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """Verify that the user_id attribute is initialized as an empty string"""
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """Verify that the name attribute is initialized as an empty string"""
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """Verify that the description attribute is initialized as an empty string"""
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        """Verify that the number_rooms attribute is initialized as 0"""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """Verify that the number_bathrooms attribute is initialized as 0"""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """Verify that the max_guest attribute is initialized as 0"""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        """Verify that the price_by_night attribute is initialized as 0"""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        """Verify that the latitude attribute is initialized as 0.0"""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attribute(self):
        """Verify that the longitude attribute is initialized as 0.0"""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        """Verify that the amenity_ids attribute is initialized as an empty list"""
        self.assertEqual(self.place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
