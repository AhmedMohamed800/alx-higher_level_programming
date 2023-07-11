#!/usr/bin/python3
"""Json Module"""
import json
"""Module of save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """returns the JSON representation of an object (string)"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
