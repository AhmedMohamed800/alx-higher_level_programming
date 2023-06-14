#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        uniq = set(my_list)
        for i in uniq:
            result += i
    return result
