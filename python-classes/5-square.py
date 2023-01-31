#!/usr/bin/python3
"""Square class"""


class Square:
    """Class defining a square with private attribute size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns square's area"""
        return self.__size ** 2

    def my_print(self):
        """Prints square to stdout with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
