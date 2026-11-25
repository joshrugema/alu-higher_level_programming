#!/usr/bin/python3
"""This module defines BaseGeometry with an area method to be overridden."""


class BaseGeometry:
    """This class is the base of all the shapes."""

    def area(self):
        """Raise an Exception: each shape must write its own area()."""
        # The base class has no shape yet, so it cannot know its area
        raise Exception("area() is not implemented")
