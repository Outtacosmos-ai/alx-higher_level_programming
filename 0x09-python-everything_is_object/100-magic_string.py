#!/usr/bin/python3

def magic_string():
    """
    Generate a string with "BestSchool" repeated a certain number of times.

    Returns:
        str: A string containing "BestSchool" repeated.
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.count)])
