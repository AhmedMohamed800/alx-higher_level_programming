#!/usr/bin/python3
"""Define a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initiate values of Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)
