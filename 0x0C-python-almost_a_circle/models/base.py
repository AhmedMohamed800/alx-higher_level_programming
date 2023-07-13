"""
==============
Module of base
==============
"""


class Base:
    """
    Base: a classe named base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Arguemtns
        ---------
        id: a unique id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
