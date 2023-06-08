#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arguments = sys.argv
arg_len = len(arguments)
result = 0
for num in range(1, arg_len):
    result += int(arguments[num])
print("{:d}".format(result))
