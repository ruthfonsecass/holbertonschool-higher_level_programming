#!/usr/bin/python3
"""Define Python interpreter path."""

class Square:
    """Class definition for a square."""

    def __init__(self, size=0):
        """Initialize Square with a default size of 0."""
        self.__size = size

    @property
    def size(self):
        """Property to get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square, with checks for int and >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' symbols or a newline if size is 0."""
        if not self.size:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
