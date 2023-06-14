#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        a_dictionary.setdefault(key, value)
    return a_dictionary
