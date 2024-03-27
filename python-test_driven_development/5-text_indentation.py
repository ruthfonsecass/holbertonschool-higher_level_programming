#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers."""

    if len(list) == 0:
        return None
    max_int = list[0]
    for num in list:
        if num > max_int:
            max_int = num
    return max_int
