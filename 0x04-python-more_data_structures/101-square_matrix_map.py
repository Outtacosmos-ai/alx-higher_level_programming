#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Compute the square of each element in a matrix using map.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: Matrix with each element squared.
    """
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
