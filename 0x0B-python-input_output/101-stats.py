#!/usr/bin/python3
""" importing """
import sys
from collections import defaultdict

def print_metrics(total_file_size, status_code_count):
    """ print metrics """
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_count.items()):
        print("{}: {}".format(status_code, count))

def main():
    """ run the command """
    total_file_size = 0
    status_code_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                ip, _, _, status_code_str, file_size_str = line.split()[:5]
                status_code = int(status_code_str)
                file_size = int(file_size_str)
                total_file_size += file_size
                status_code_count[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_metrics(total_file_size, status_code_count)

            except ValueError:
                pass

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_count)

if __name__ == "__main__":
    main()
