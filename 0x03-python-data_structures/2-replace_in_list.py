#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces the element at the specified index in the list.
    If the index is out of range, returns the original list.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
