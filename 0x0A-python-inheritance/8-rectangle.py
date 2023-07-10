#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module of BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle(BaseGeometry)"""
    def __init__(self, width, height):
        self.integer_validator("width", height)
        self.__width = width
        self.integer_validator("height", height)
        self.__hiegth = height
