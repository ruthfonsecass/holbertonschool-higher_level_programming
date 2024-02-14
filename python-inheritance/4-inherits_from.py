#!/usr/bin/python3
"""A module with a class MyList that inherits from class list"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
