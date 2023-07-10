#!/usr/bin/python3
"""Module of MyList class"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        print(sorted(self))
