#!/usr/bin/python3
"""Module to read command line's arguments"""
import sys
from os.path import exists
"""Module of add_item"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

listy = sys.argv
listy.pop(0)
if exists("add_item.json"):
    x = load_from_json_file("add_item.json")
    x.extend(listy)
    save_to_json_file(x, "add_item.json")
else:
    save_to_json_file(listy, "add_item.json")
