#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        int: The number of elements printed.
    """
    # Initialize the count of printed elements
    elements_printed = 0

    # Check if my_list is provided, if not, use an empty list
    if my_list is None:
        my_list = []

    # Iterate through the list to print elements
    for i in range(x):
        try:
            # Print the element without a newline
            print("{}".format(my_list[i]), end="")

            # Increment the count of printed elements
            elements_printed += 1
        except IndexError:
            # Stop printing if index is out of bounds
            break

    # Print a newline after printing all elements
    print("")

    return elements_printed
