#!/usr/bin/python3
"""Module of class_to_json"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return vars(obj)
