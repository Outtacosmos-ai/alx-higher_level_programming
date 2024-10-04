#!/usr/bin/python3
"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle of n.

    Returns a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
