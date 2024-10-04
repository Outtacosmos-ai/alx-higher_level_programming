#!/usr/bin/python3
"""Script for parsing HTTP request logs."""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics.

    Args:
        total_size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) > 2:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
