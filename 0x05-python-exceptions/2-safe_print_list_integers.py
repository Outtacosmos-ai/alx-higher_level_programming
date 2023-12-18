#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    """Print the first x elements of a list that are integers.

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

    # Iterate through the list to print integer elements
    for i in range(0, x):
        try:
            # Print the integer element without a newline
            print("{:d}".format(my_list[i]), end="")

            # Increment the count of printed elements
            elements_printed += 1
        except (ValueError, TypeError):
            # Continue to the next element if it's not an integer
            continue

    # Print a newline after printing all elements
    print("")

    return elements_printed
