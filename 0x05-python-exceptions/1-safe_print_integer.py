#!/usr/bin/python3

def safe_print_integer(value):
    try:
        my_value = int(value)
    except ValueError:
        return False
    print("{:d}".format(my_value))
    return True
