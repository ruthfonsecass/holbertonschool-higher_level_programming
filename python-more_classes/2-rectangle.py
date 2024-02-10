#!/usr/bin/python3
"""Define Python interpreter path."""
class Rectangle:
    """Class definition for a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with width and height."""
        self.__width = width
        self.__height = height

@property
def width(self):
    """Get the height of the rectangle."""
    return self.__width

@width.setter
def width(self, value):
    if type(value) is not int:
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
    """Set the height of the rectangle, ensuring it's a non-negative integer."""
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = value

def area(self):
    """Calculate and return the area of the rectangle."""
    return self.__height * self.__width

def perimeter(self):
    """Calculate and return the perimeter of the rectangle."""
    return 2 * (self.__height + self.__width)
