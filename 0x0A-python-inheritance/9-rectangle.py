#!/usr/bin/python3
"""teasdasd"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module of BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle(BaseGeometry)"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"[Rectangle] {self.width}/{self.height}"
