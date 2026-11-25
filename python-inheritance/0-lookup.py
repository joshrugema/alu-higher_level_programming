#!/usr/bin/python3
"""This module defines a function that lists what an object can do."""


def lookup(obj):
    """Return a list with every attribute and method name of obj.

    Args:
        obj: the object (or class) to look inside.
    """
    # dir() gives back all the names an object knows, as a list
    return dir(obj)
