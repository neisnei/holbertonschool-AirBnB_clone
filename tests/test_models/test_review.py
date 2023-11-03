#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_place_id_attribute(self):
        """ Verify that the place_id attribute is initialized
        as an empty string"""
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """Verify that the user_id attribute is initialized
        as an empty string"""
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """Verify that the text attribute is initialized as an empty string"""
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
