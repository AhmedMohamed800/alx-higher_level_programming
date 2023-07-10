#!/usr/bin/python3
"""Module of BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    @classmethod
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    @classmethod
    def area(self):
        raise Exception("area() is not implemented")
