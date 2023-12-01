#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints the elements of a list in reverse order.
    If the list is empty, nothing is printed.
    """
    if my_list:
        for i in reversed(my_list):
            print('{:d}'.format(i))
