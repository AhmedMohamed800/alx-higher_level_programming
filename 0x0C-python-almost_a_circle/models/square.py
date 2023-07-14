"""
================
Module of Square
================
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square: define a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Define square attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """print object as string"""
        return f"[Square] ({self.id} {self.x}/{self.y} - {self.size})"
