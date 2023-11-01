#!/usr/bin/python3
"""This module defines a class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """City class that inherits from BaseModel
    Attributes:
        name (str): The state name."""
    name = ""
