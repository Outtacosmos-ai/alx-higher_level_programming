#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Finds the elements that are unique to each set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the unique elements from each set.
    """
    return set_1 ^ set_2
