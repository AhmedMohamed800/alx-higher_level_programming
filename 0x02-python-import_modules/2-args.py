#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arguments = sys.argv
arg_len = len(arguments)
message = "argument"

if arg_len == 1:
    message += "s."
elif arg_len == 2:
    message += ":"
elif arg_len > 2:
    message += "s:"
print("{:d} {:s}".format(arg_len - 1, message))
for num in range(1, arg_len):
    print("{:d}: {:s}".format(num, arguments[num]))
