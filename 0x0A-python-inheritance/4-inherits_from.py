#!/usr/bin/python3
"""Module of inherits_from"""


def inherits_from(obj, a_class):
    """object is an instance of a class"""
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
