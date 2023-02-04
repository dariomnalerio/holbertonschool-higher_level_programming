#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Class defining a rectangle with attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            per = 0
        else:
            per = self.width * 2 + self.height * 2
        return per

    def __str__(self):
        rect = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                rect += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) == 0:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) == 0:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2