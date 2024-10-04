#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Calculate the area of the geometry object."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
