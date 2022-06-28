#!/usr/bin/python3
"""Defines a Rectangle object."""


class Rectangle:
    """Represent a Rectangle.

    Attributes:
        number_of_instances (int): The number of instances of Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the.
        """

        self.__width = width
        self.__height = height

        type(self).number_of_instances += 1

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
        """Returns Area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("##")
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns a string representation of the rectangle.
            Representa the Rectangle with ##."""

        if self.__width == 0 or self.__height == 0:

            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ method: __del__
            deletes instance of Rectangle class and prints bye message
        """

        type(self).number_of_instances -= 1
        print("Bye Rectangle...")
