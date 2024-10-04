#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics.

It calculates the total file size and counts occurrences of
specific HTTP status codes. The script prints these statistics
every 10 lines and/or when interrupted by CTRL+C.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print the accumulated statistics.

    Args:
        total_size (int): The total file size processed so far.
        status_codes (dict): A dictionary with status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parse a single line of the input.

    Args:
        line (str): A line from the input.

    Returns:
        tuple: A tuple containing the status code and file size,
               or (None, None) if the line is invalid.
    """
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None


def main():
    """
    Main function to process the input and print statistics.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
