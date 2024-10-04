#!/usr/bin/python3
"""Module for reading a text file and printing its content."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
