#!/usr/bin/python3
"""This module defines a class Square that checks its size."""


class Square:
    """This class represents a square with a checked private size."""

    def __init__(self, size=0):
        """Create a new square after checking the size.

        Args:
            size: the length of one side of the square, 0 by default.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        # Check the type first (TypeError), then the value (ValueError)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        # __size (two underscores) = private: Python renames it _Square__size
        self.__size = size
