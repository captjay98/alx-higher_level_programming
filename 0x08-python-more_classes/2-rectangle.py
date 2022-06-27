#!/usr/bin/python3
"""Defines a Rectangle object."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle."""

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
        """Get/Set height of the Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))