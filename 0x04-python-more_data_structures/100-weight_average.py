#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Args:
        my_list (list): List of tuples where each tuple contains two elements:
                        (value, weight).

    Returns:
        float: Weighted average or 0 if the list is empty.
    """
    if my_list and len(my_list):
        numerator = 0
        denominator = 0

        for value, weight in my_list:
            numerator += value * weight
            denominator += weight

        return numerator / denominator

    return 0
