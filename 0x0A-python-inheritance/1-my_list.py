#!/usr/bin/python3
"""Module of MyList class"""


class MyList(list):
    """inherits from list"""
    pass

    def print_sorted(self):
        return sorted(list(self))
