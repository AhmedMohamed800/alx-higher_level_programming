#!/usr/bin/python3
"""Json Module"""
import json
"""Module of from_json_string"""


def from_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.loads(my_obj)
