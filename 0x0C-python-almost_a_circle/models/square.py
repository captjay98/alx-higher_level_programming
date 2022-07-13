#!/usr/bin/python3
"""imports from rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square Class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns details on the square"""
        return ("[Square] (<{}>) <{}>/(<{}>) - <{}>"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
