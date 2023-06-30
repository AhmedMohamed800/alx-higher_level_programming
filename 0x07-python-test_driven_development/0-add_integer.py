#!/usr/bin/python3
"""Mondule for add_intger"""


def add_integer(a, b=98):
    """give the sum of a + b

    Arguments:
        a: first integer
        b: second integer

    Raises:
        TypeError if a or b isn't int or float
    Returns :the sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
