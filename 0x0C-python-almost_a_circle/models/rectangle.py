#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    """Creates a Rectangle Class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns Private attribute of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private attribute of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns Private attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private attribute of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns Private attribute of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets private attribute of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns Private attribute of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets private attribute of x"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
