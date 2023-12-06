#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square of each element in a 2D matrix.

    Args:
        matrix (list of lists): The input 2D matrix.

    Returns:
        list of lists: The resulting matrix with squared elements.
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
