#!/usr/bin/python3
"""This module defines a class Rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle with a width and a height."""

    def __init__(self, width, height):
        """Create a new rectangle after checking width and height.

        Args:
            width: the width, a positive integer.
            height: the height, a positive integer.
        """
        # integer_validator comes with BaseGeometry (inherited), so self has it
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
