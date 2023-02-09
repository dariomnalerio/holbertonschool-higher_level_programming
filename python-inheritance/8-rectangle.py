#!/usr/bin/python3
"""" Class BaseGeometry """


class BaseGeometry:
    """ Class defining a BaseGeometry object """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


""" Class Rectangle """


class Rectangle(BaseGeometry):
    """" Class defining a Rectangle object """
    def __init__(self, width, height):
        Rectangle.integer_validator(self, "height", height)
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height
