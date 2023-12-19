#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The side length of the square.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The side length of the square.
        """
        self.size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
