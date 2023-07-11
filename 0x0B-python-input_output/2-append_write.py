#!/usr/bin/python3
"""Module of append_file"""


def append_write(filename="", text=""):
    """writes a string (UTF8) and prints it to stdout"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
