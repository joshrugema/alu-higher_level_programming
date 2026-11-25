#!/usr/bin/python3
"""This module defines a class Square that can print itself with #."""


class Square:
    """This class represents a square that can be printed."""

    def __init__(self, size=0):
        """Create a new square with the given size.

        Args:
            size: the length of one side of the square, 0 by default.
        """
        # Goes through the setter, so the checks run here too
        self.size = size

    # @property = getter: runs when you read my_square.size
    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    # setter: runs when you write my_square.size = value
    @size.setter
    def size(self, value):
        """Set the size of the square after checking the value.

        Args:
            value: the new length of one side of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        # Check the type first (TypeError), then the value (ValueError)
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square, which is size times size."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character, or an empty line."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            # "#" * 3 repeats the string: "###"
            print("#" * self.__size)
