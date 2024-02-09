#!/usr/bin/python3
def __init__(self, width=0, height=0):
    self.__width = width
    self.__height = height

@property
def width(self):
    return self.__width

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("idth must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = value

@property
def height(self):
    return self.__height

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = value
        return self.__height

def area(self):
    return self.__height * self.__width

def perimeter(self):
    if self.__height == 0 and self.__width == 0:
        return 0
    else:
        return 2 * (self.__height + self.__width)

def __str__(self):
    rectangle = ""

    if self.width == 0 or self.height == 0:
        return rectangle
    
    for i in range(self.height):
        rectangle += ("#" * self.width) + "\n"

    return rectangle[:-1]