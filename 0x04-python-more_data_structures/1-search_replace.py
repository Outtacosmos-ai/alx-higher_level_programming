#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Searches for a specific element in a list and replaces it with another.

    Args:
        my_list (list): The input list.
        search: The element to search for.
        replace: The element to replace 'search' with.

    Returns:
        list: A new list with the specified replacements.
    """
    def find_search(element):
        return element if element != search else replace

    return list(map(find_search, my_list))
