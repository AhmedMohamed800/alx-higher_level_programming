"""
==============
Module of base
==============
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
