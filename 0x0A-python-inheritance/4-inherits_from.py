#!/usr/bin/python3
"""Module of inherits_from"""


def inherits_from(obj, a_class):
    """object is an instance of a class"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
