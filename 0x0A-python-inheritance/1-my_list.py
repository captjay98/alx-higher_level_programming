#!/usr/bin/python3
""" Returns a List Sorted in Ascending Order"""


class MyList(list):
    """ Represents a MyList"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
