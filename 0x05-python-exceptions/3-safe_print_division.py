#!/usr/bin/python3

def safe_print_division(a, b):
    """Prints the division of a by b, or None if division is not possible."""
    try:
        print("Inside result: {}".format(a / b))
    except (TypeError, ZeroDivisionError):
        print("Inside result: None")
        return None
    return a / b
