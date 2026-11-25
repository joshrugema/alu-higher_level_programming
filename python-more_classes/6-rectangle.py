#!/usr/bin/python3
"""This module defines a class Rectangle that counts its instances."""


class Rectangle:
    """This class represents a rectangle."""

    # Class attribute: one value shared by every rectangle
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Create a new rectangle with a width and a height.

        Args:
            width: the width of the rectangle, 0 by default.
            height: the height of the rectangle, 0 by default.
        """
        # Height first, so __dict__ shows height before width
        self.height = height
        self.width = width
        # Count one more rectangle (on the class, not on self)
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the area of the rectangle (width times height)."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if a side is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with #, used by print() and str()."""
        # __str__ RETURNS the text; print() is what shows it
        if self.__width == 0 or self.__height == 0:
            return ""
        text = ""
        for i in range(self.__height):
            # "#" * 3 repeats the string: "###"
            text = text + "#" * self.__width
            # A new line after every row except the last one
            if i < self.__height - 1:
                text = text + "\n"
        return text

    def __repr__(self):
        """Return a string that eval() can use to recreate the rectangle."""
        # eval("Rectangle(2, 4)") builds a new, equal rectangle
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and count one less rectangle when deleted."""
        # __del__ runs when the rectangle is deleted (del or end of program)
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
