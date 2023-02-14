#!/usr/bin/python3
"""" Module containing rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Class defining a rectangle, inheriting from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def heigth(self):
        return self._height

    @heigth.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self._y = value
