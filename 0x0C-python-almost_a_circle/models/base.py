#!/usr/bin/python3
""" Base Class for all other objects in this Project"""


class Base:
    """A base class to manage other classes created
    @id: The id for a specific instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """new """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
