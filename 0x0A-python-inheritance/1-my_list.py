#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the list class.
"""


class MyList(list):
    """A custom class that inherits from the list class."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
