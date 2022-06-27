#!/usr/bin/python3
"""Defines a Rectangle object"""


class Rectangle:
    """A Rectangle object"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object
        Args:
            width(int): The width of the rectangle
            height(int): The height of the
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("eight must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
