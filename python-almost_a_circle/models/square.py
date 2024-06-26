#!/usr/bin/python3
"""A module with a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """A constructor method for the Square class
        """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value