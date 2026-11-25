#!/usr/bin/python3
"""This module defines a function that checks if an object is a child."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class, not a_class.

    Args:
        obj: the object to check.
        a_class: the parent class to look for.
    """
    # isinstance() = a_class or a child, type() is not a_class = not itself
    # Both true means: a child only
    return isinstance(obj, a_class) and type(obj) is not a_class
