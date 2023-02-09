#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Class Rectangle """


class Rectangle(BaseGeometry):
    """" Class defining a Rectangle object """
    def __init__(self, width, height):
        Rectangle.integer_validator(self, "height", height)
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height
