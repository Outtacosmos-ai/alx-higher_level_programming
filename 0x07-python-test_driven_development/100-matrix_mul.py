def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Raises:
        TypeError: If inputs are not valid matrices.
        ValueError: If matrices cannot be multiplied.

    Returns:
        list of lists of int/float: Result of the matrix multiplication.
    """
    if not all(isinstance(matrix, list) for matrix in (m_a, m_b)):
        raise TypeError("Both matrices must be lists of lists")

    if any(
        not all(isinstance(element, (int, float)) for element in row)
        for row in m_a + m_b
    ):
        raise TypeError("Matrices should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a + m_b):
        raise TypeError("All rows in a matrix must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices cannot be multiplied")

    transposed_b = [[row[i] for row in m_b] for i in range(len(m_b[0]))]
    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in transposed_b]
        for row_a in m_a
    ]

    return result
