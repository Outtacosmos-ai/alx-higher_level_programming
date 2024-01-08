#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """Check if the object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class, False otherwise.
    """
    return isinstance(obj, a_class)
