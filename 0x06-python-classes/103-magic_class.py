#!/usr/bin/python3
"""Define a class for magical calculations"""
import math


class MagicClass:
    """Set up the magic"""

    def __init__(self, radius=0):
        """Initialize the MagicClass.

        Args:
            radius (int or float): The radius for magical calculations.
                Default is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the magic.

        Returns:
            float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the magic.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
