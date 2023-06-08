#!/usr/bin/python3
import hidden_4

if __name__ != "__main__":
    exit()

for str in dir(hidden_4):
    if str[0:2] != '__':    
        print("{:s}".format(str))
