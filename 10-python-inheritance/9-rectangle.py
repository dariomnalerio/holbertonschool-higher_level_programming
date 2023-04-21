#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """" Class defining a Rectangle object """
    def __init__(self, width, height):
        Rectangle.integer_validator(self, "height", height)
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
