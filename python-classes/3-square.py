#!/usr/bin/python3
"""Define Python interpreter path."""

class Square:
    """Class definition for a square."""

    def __init__(self, size=0):        
        if type(size) is not int:
            """Check if size is not an integer."""
            raise TypeError("size must be an integer")
            
        elif size < 0:
            """Check if size is negative."""
            raise ValueError("size must be >= 0")
        
        else:
            self.__size = size
            """Assign size to a private instance variable if checks pass."""
    def area(self):
        return self.__size * self.__size
