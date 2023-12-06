#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in the list by the given number using map.

    Args:
        my_list (list): List of numbers.
        number (int): The multiplier.

    Returns:
        list: New list with elements multiplied by the specified number.
    """
    return list(map(lambda x: x * number, my_list))
