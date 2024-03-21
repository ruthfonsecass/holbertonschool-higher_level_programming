#!/usr/bin/python3
"""Define Python interpreter path."""

def add_integer(a, b=98):
    """Add two integers or floats, converting floats to integers before addition.
    
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float. Defaults to 98.

    Returns:
        The sum of a and b, with both treated as integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    else:
        type(b) is float
        b = int(b)
    return a + b