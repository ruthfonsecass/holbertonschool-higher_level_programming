#!/usr/bin/python3
"""A module with a Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x position of the Recangle
            y (int): the y position of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


@property
def width(self):

    """Gets the height of the Rectangle"""
    return self.__width


@width.setter
def width(self, value):
    if type(value) is not int:
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be > 0")
    else:
        self.__width = value


@property
def heigth(self):
    """Gets the height of the Rectangle"""
    return self.__heigth


@heigth.setter
def heigth(self, value):
    if type(value) is not int:
        raise TypeError("heigth must be an integer")
    if width <= 0:
        raise ValueError("heigth must be > 0")
    else:
        self.__heigth = value


@property
def x(self):
    return self.__x


@x.setter
def x(self, value):
    """Sets the height of the Rectangle"""
    if type(value) is not int:
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be >= 0")
    else:
        self.__x = value


@property
def y(self):
    return self.__y


@y.setter
def y(self, value):
    if type(value) is not int:
        raise TypeError("y must be an integer")
    if y < 0:
        raise ValueError("y must be >= 0")
    else:
        self.__y = value
