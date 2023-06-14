#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        listy = my_list.copy()
        for x in range(len(listy)):
            if listy[x] == search:
                listy[x] = replace
    return listy
