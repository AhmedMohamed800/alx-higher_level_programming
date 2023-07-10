#!/usr/bin/python3
"""Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle
"""Module of BaseGeometry"""


class Square(Rectangle):
    """ SQUARE"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
