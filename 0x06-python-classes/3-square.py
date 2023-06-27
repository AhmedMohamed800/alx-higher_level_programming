#!/usr/bin/python3
""" The file is a continue of the previous task"""


class Square:
    """defines a square by based on 1-square.py"""
    def __init__(self, size=0):
        """
        defines the variables of Square

        Args:
            self: the self argument of the class
            size: square's size

        Returns:
            noting
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """
        calculate the current square area

        Args:
            self: the self arugment of the class

        Returns:
            returns the current square area

        """
        return self.__size * self.__size
