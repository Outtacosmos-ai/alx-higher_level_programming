#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for idx, column in enumerate(row):
            print('{:d}'.format(column), end='')
            if idx < len(row) - 1:
                print(' ', end='')
        print()
