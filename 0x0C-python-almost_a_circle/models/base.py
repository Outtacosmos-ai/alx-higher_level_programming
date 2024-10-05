#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class

        Args:
            id (int): The identifier of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
