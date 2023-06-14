#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_dict = list(a_dictionary.keys())
        sorted_dict.sort()
        for ele in sorted_dict:
            print(f"{ele}: {a_dictionary[ele]}")
