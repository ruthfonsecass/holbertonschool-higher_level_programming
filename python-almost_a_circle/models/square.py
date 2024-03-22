#!/usr/bin/python3
"""A module with a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """A constructor method for the Square class

        Args:
            size (int): the size of the Square
            x (int): the x position of the Square
            y (int): the y position of the Square
            id (int): the identity of the new Square
        """
        super().__init__(size, size, x, y, id)