#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Create a Square.

        Args:
            size (int): Length of a side of Square.
        """
        self.__size = size

    @property
    def size(self):
        """The property of size as the length of a side of Square.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of Square.

        Args:
            value (int): The size.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square.

        Returns:
            int: The size squared.
        """
        return self.__size * self.__size

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()
