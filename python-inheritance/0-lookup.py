#!/usr/bin/python3
"""A simple module with a function that returns the list
of availables attributes and methods of an object
"""


def lookup(obj):
    """returns a list of names of an object's attributes and methods."""
    return dir(obj)
