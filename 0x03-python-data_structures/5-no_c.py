#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    for stri in my_string:
        if stri != "c" and stri != "C":
            str += stri
    return str
