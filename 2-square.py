#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size(int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("Square size must be an integer")
        elif size < 0:
            raise ValueError("Square size must be >= 0")

        self.__size = size
