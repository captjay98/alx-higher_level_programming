#!/usr/bin/python3
""" Function that returns a list of available Attributes"""


def lookup(obj):
    """ function: lookup()
    Returns a list object
    """
    return dir(obj)
