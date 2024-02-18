#!/usr/bin/python3
"""A module with a class inherits_fromthat inherits from class list"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
