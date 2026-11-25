#!/usr/bin/python3
"""This module defines BaseGeometry with an integer validator."""


class BaseGeometry:
    """This class is the base of all the shapes."""

    def area(self):
        """Raise an Exception: each shape must write its own area()."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name: the name of the value, used in the error message.
            value: the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        # type() and not isinstance(): True is a bool, and bool is a
        # child of int, so isinstance(True, int) would let it through
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
