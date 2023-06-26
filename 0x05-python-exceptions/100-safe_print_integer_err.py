#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    message = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        return True
    except (ValueError):
        sys.stderr.write(message)
        return False
