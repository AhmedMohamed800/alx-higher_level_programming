#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_listy = my_list.copy()
    if not (idx > len(new_listy) - 1) and not (idx < 0):
        new_listy[idx] = element
    return new_listy
