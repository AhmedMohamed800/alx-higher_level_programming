#!/usr/bin/python3
"""Module of write_file"""


def write_file(filename="", text=""):
    """writes a string (UTF8) and prints it to stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
