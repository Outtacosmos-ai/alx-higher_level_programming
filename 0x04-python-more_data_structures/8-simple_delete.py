#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
