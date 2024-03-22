#!/usr/bin/python3
"""A module with a Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the height of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets the height of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets the height of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Public method that returns the area value
        of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self) -> str:
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)


    def to_dictionary(self):
            """Public method that returns the dictionary representation
            of a Rectangle
            """
            return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }