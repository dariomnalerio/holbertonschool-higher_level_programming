#!/usr/bin/python3
"""Square class"""


class Square:
    """Class defining a square with private attribute size"""
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns square's area"""
        return self.__size ** 2