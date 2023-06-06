#!/usr/bin/python3
for i in range(10):
    for y in range(1, 10):
        if y != i and y > i:
            print(f"{i}{y}", end=", " if i != 8 or y != 9 else "\n")
