#!/usr/bin/python3
"""Define Python interpreter path."""

class Square:
    """Class definition for a square."""

    def __init__(self, size=0):
        """Initialize Square with a size."""
        self.__size = size

    @property
    def size(self):
        """Property to get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square, with checks for int and non-negative values."""
        if not isinstance(value, int):
            """Check if value is not an integer."""
            raise TypeError("size must be an integer")
            
        elif value < 0:
            """Check if value is negative."""
            raise ValueError("size must be >= 0")
            
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size
