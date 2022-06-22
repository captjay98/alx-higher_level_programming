#!/usr/bin/python3
"""Define a Class Square."""


class Square():
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size( int): The size of the new square.
        """
        self.size = size

        @property
        def size(self):
            """Get/Set the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return the area of the square"""
            return (self.__size * self.__size)
