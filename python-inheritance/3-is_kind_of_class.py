#!/usr/bin/python3
"""This module defines a function that checks the family of an object."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    # isinstance() says yes for the class itself AND for its children
    return isinstance(obj, a_class)
