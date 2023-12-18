#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer using "{:d}".format().

    If a ValueError occurs, print the exception message to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if successful, False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print(f"Exception: {error}", file=sys.stderr)
        return False
