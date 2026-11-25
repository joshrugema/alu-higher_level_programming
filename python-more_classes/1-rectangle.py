#!/usr/bin/python3
"""This module defines a class Rectangle with a width and a height."""


class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Create a new rectangle with a width and a height.

        Args:
            width: the width of the rectangle, 0 by default.
            height: the height of the rectangle, 0 by default.
        """
        # Height first, so __dict__ shows height before width
        self.height = height
        self.width = width

    # @property = getter: runs when you read my_rectangle.width
    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    # setter: runs when you write my_rectangle.width = value
    @width.setter
    def width(self, value):
        """Set the width after checking it is an integer >= 0.

        Args:
            value: the new width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        # Check the type first (TypeError), then the value (ValueError)
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # @property = getter: runs when you read my_rectangle.height
    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    # setter: runs when you write my_rectangle.height = value
    @height.setter
    def height(self, value):
        """Set the height after checking it is an integer >= 0.

        Args:
            value: the new height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
