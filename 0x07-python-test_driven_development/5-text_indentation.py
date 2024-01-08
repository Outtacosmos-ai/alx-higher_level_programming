#!/usr/bin/python3

"""
This module contains a function that indents texts.
"""


def text_indentation(text):
    '''
    This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0

    # Skip leading spaces
    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        print(text[count], end="")

        # Check for newline or specific punctuation
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1

            # Skip trailing spaces
            while count < len(text) and text[count] == " ":
                count += 1
            continue

        count += 1


# Example usage
text = "Sample text with sentences ending in dot, question mark, or colon."
text_indentation(text)
