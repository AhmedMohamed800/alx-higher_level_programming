#!/usr/bin/python3
"""Json Module"""
import json
"""Module of save_to_json_file"""


def load_from_json_file(filename):
    """returns the JSON representation of an object (string)"""
    with open(filename, "r") as f:
        return json.load(f)
