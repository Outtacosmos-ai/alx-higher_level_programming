#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds unique elements from a list.

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique elements.
    """
    number = 0
    for element in set(my_list):
        number += element
    return number
