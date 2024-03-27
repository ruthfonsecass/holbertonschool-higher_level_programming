#!/usr/bin/python3
"""Define Python interpreter path."""

def print_square(size):
    """Prints a square of a given size using the '#' character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
