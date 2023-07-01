#!/usr/bin/python3
"""This module is for print_square"""


def print_square(size):
    """
    prints a square with the character #

    Arguments:
        size: size of square

    Returns: nothing
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
