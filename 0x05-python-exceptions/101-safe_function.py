#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(func, *args):
    """Safely executes a function and handles exceptions.

    Args:
        func (callable): The function to be executed.
        *args: Variable number of arguments to pass to the function.

    Returns:
        The result of the function if successful, otherwise None.
    """
    try:
        result = func(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    else:
        return result
