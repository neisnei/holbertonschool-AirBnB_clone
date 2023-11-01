#!/usr/bin/python3
"""This module defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel
    Attributes:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): The review text."""
    place_id = ""
    user_id = ""
    text = ""
