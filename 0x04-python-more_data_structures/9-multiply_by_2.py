#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiplies each value in the dictionary by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: The updated dictionary.
    """
    return {key: val * 2 for key, val in a_dictionary.items()}
