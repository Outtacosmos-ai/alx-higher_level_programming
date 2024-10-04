#!/usr/bin/python3
"""This module defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This class represents a base geometry."""

    def area(self):
        """Method not implemented yet.

        Raises:
            Exception: Always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

            Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
