#!/usr/bin/python3
"""A module with a class is_same_class that inherits from class list"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance
    of the specified class ;
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
