#!/usr/bin/python3
"""
A module with an empty BaseGeometry class
"""


class BaseGeometry:
    """This is the BaseGeometry class."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
