#!/usr/bin/python3
"""Module for saving an object to a file using JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)