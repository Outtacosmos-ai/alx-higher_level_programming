#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b or None if division is not possible."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
