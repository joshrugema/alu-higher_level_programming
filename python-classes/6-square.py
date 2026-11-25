#!/usr/bin/python3
"""This module defines a class Square with a size and a position."""


class Square:
    """This class represents a square that is printed at a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a new square with a size and a position.

        Args:
            size: the length of one side of the square, 0 by default.
            position: a tuple of 2 positive integers, (0, 0) by default.
        """
        # Goes through the setter, so the checks run here too
        self.size = size
        self.position = position

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

    # @property = getter: runs when you read my_square.position
    @property
    def position(self):
        """Return the current position of the square."""
        return self.__position

    # setter: runs when you write my_square.position = value
    @position.setter
    def position(self, value):
        """Set the position of the square after checking the value.

        Args:
            value: a tuple of 2 positive integers (spaces, empty lines).

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        # Three checks: a tuple of 2 items, both ints, both >= 0
        message = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(message)
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(message)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(message)
        self.__position = value

    def area(self):
        """Return the area of the square, which is size times size."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #, moved by the position with spaces."""
        if self.__size == 0:
            print("")
            return
        # position[1] = empty lines above the square
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            # position[0] = spaces before each row; "#" * 3 gives "###"
            print(" " * self.__position[0] + "#" * self.__size)
