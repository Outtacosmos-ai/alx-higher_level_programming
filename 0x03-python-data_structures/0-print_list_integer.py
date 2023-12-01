#!/usr/bin/python3

def print_list_integer(my_list=None):
    """Prints each integer in the given list."""
    if my_list is None:
        my_list = []

    for number in my_list:
        print('{:d}'.format(number))
