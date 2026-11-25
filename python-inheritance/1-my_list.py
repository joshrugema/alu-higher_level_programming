#!/usr/bin/python3
"""This module defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list with one extra method, print_sorted.

    MyList(list) means MyList inherits everything a list can do
    (append, len, print...) and we only add what is new.
    """

    def print_sorted(self):
        """Print the list sorted in ascending order, without changing it."""
        # sorted() builds a NEW list, so self keeps its original order
        print(sorted(self))
