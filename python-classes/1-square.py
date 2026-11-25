#!/usr/bin/python3
"""This module defines a class Square that stores its size."""


class Square:
    """This class represents a square with a private size."""

    def __init__(self, size):
        """Create a new square with the given size.

        Args:
            size: the length of one side of the square.
        """
        # __size (two underscores) = private: Python renames it _Square__size
        self.__size = size
