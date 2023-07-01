#!/usr/bin/python3
""" This Module is for say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Arguments:
        first_name: first name of a person
        last_name: last name of a person

    Returns:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
