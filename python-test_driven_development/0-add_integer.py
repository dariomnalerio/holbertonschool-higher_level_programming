#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is not float and type(a) is not int or a is None:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
