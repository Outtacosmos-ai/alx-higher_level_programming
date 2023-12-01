#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete the element at a specific position in the list."""
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
