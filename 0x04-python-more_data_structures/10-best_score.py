#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = 0
        for key in a_dictionary:
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                elemento = key
        return elemento
    return None
