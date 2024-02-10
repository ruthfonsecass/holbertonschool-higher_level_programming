#!/usr/bin/python3
"""Define Python interpreter path."""

def print_square(size):
    """Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square's sides. Must be an integer >= 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if type(size) not in int:
        raise TypeError("size must be an integer")
    if size < 0:
    
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
