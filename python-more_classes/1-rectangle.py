#!/usr/bin/python3
"""Define Python interpreter path."""


class Rectangle:
    """Class definition for a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not (int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
