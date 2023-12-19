#!/usr/bin/python3
"""A module that defines a square."""


class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializing the Square class.

        Args:
            size (int): Represents the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The square of the size.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
