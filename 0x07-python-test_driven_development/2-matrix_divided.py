#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and rounds the result to 2 decimal places.
    
    Args:
        matrix (list of lists): A matrix represented as a list of lists, 
                                where each inner list contains integers or floats.
        div (int/float): The divisor, which must be an integer or a float.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if the rows of the matrix are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    
    # Validate the matrix is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Ensure all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate the divisor is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the division and round each result to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]
