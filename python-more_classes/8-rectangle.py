#!/usr/bin/python3
"""This module defines a class Rectangle that compares two rectangles."""


class Rectangle:
    """This class represents a rectangle."""

    # Class attribute: one value shared by every rectangle
    number_of_instances = 0
    # Class attribute: the symbol used to draw, "#" unless changed
    print_symbol = "#"

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
        """Return the rectangle drawn with print_symbol, used by print()."""
        # __str__ RETURNS the text; print() is what shows it
        if self.__width == 0 or self.__height == 0:
            return ""
        # self.print_symbol looks on the instance first, then the class
        # str() turns any type (like a list) into text first
        symbol = str(self.print_symbol)
        rows = []
        for i in range(self.__height):
            rows.append(symbol * self.__width)
        # Join the rows with new lines, no new line after the last row
        return "\n".join(rows)

    def __repr__(self):
        """Return a string that eval() can use to recreate the rectangle."""
        # eval("Rectangle(2, 4)") builds a new, equal rectangle
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and count one less rectangle when deleted."""
        # __del__ runs when the rectangle is deleted (del or end of program)
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # @staticmethod: no self or cls, it only works on what you pass in
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area, rect_1 if equal.

        Args:
            rect_1: the first rectangle.
            rect_2: the second rectangle.

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        # >= so that rect_1 wins a tie
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
