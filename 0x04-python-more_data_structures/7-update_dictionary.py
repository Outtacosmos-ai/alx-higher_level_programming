#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates or adds a key-value pair in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to update or add.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
