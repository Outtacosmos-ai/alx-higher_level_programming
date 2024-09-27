#!/usr/bin/python3
"""
Module that defines the add_integer function.
This function adds two integers or floats, casting them to integers if needed.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: First integer or float.
        b: Second integer or float, defaults to 98.

        Returns:
        The sum of a and b as an integer.

        Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
