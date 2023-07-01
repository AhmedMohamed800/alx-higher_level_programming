#!/usr/bin/python3
"""Module of matrix_divided"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Arguments:
        matrix: a matrix 2D list
        div: the number with which the whole list will be divded

    Returns:
        a new list with its element divded
    """
    new_list = []
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if type(matrix) is not list or not (matrix):
        raise TypeError(message)

    if matrix[0]:
        x = len(matrix[0])
    for i in range(0, len(matrix)):
        if type(matrix[i]) is not list or not (matrix[i]):
            raise TypeError(message)
        new_list.append([])
        if x != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) not in [float, int]:
                raise TypeError(message)
            new_list[i].append(round(matrix[i][j] / div, 2))

    return new_list
