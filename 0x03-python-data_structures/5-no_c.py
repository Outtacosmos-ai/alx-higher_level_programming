#!/usr/bin/python3

def no_c(my_string):
    """Remove 'c' and 'C' from the input string."""
    updated_str = ''.join(char for char in my_string if char.lower() != 'c')
    return updated_str
