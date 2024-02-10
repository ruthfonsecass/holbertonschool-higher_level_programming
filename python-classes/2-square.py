#!/usr/bin/python3
"""Specify Python interpreter path."""


class Square:
    """Defines a class Square."""

    def __init__(self, size=0):
        """Initializes Square with a default size of 0, ensuring size is an int and >= 0."""

        if not isinstance(size, int):
            """Check if size is not an integer."""
            raise TypeError("size must be an integer")
  
        if size < 0:
            """Check if size is less than 0."""
            raise ValueError("size must be >= 0")
        else:
            self.size = size
