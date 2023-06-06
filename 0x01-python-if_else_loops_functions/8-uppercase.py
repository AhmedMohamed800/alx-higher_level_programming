#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            upper = chr(ord(char) - 32)
            print(f"{upper}", end="")
        else:
            print(f"{char}", end="")
    print()
