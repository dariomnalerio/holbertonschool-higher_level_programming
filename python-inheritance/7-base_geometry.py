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
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
