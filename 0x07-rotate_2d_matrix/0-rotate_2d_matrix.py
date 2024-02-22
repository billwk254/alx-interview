#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a two-dimensional matrix 90 degrees clockwise in place.

    Args:
        matrix (list): A two-dimensional matrix represented as a list of lists.

    Returns:
        None
    """
    n = len(matrix)
    for i in range(n // 2):
        # Calculate the last index in the current layer
        last = n - 1 - i
        for j in range(i, last):
            # Calculate the relative index from the last index
            offset = j - i
            # Store the current element in a temporary variable
            temp = matrix[i][j]
            # Move values from right to top
            matrix[i][j] = matrix[last - offset][i]
            # Move values from bottom to right
            matrix[last - offset][i] = matrix[last][last - offset]
            # Move values from left to bottom
            matrix[last][last - offset] = matrix[j][last]
            # Move values from top to left
            matrix[j][last] = temp
