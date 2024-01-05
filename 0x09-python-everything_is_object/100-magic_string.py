#!/usr/bin/python3

def magic_string():
    """Generate a magic string.

    Returns:
    str: A string with "BestSchool" repeated a certain number of times.
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.count)])
