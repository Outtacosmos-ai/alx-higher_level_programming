#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the highest value in the dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        str or None: The key with the highest value or None if the dictionary is empty.
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
