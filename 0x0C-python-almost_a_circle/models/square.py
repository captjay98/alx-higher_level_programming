#!/usr/bin/python3
"""imports from rectangle class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square Class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns details on the square"""
        return ("[Square] (<{}>) <{}>/(<{}>) - <{}>"
                .format(self.id, self.x, self.y, self.width))
