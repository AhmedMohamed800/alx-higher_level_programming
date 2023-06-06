#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper = ord(char)
        if upper in range(97, 123):
            upper = upper - 32
        print("{}".format(chr(upper)), end="")
    print()
