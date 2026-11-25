#!/usr/bin/python3
"""This module defines a class Square that prints itself as a square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square: a rectangle with equal sides."""

    def __init__(self, size):
        """Create a new square after checking size.

        Args:
            size: the length of each side, a positive integer.
        """
        self.integer_validator("size", size)
        # super() runs Rectangle's __init__, so width = height = size
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square (size times size)."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description: [Square] width/height."""
        # Overrides Rectangle's __str__, which would say [Rectangle]
        return "[Square] {}/{}".format(self.__size, self.__size)
