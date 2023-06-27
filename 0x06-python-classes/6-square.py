#!/usr/bin/python3
""" The file is a continue of the previous task"""


class Square:
    """defines a square by based on 1-square.py"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size <= 0:
            print()
