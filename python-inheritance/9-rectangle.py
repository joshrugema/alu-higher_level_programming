#!/usr/bin/python3
"""This module defines a full class Rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle with a width and a height."""

    def __init__(self, width, height):
        """Create a new rectangle after checking width and height.

        Args:
            width: the width, a positive integer.
            height: the height, a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle (width times height)."""
        # This area() overrides the one in BaseGeometry that raised
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description: [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
