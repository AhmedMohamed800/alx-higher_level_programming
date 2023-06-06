#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            upper = chr(ord(char) - 32)
            print("{}".format(upper), end="" if str[-1] != char else "\n")
        else:
            print("{}".format(char), end="" if str[-1] != char else "\n")
