#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    nummies = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    nummy = 0
    prev = "M"
    for i in range(len(roman_string)):
        if i != 0:
            prev = roman_string[i - 1]
        current = roman_string[i]
        if i + 1 != len(roman_string):
            next_e = roman_string[i + 1]
        else:
            next_e = current
        if nummies[current] > nummies[prev]:
            nummy += nummies[current] - 1
            continue
        if nummies[current] > nummies[next_e]:
            nummy += nummies[current]
        if nummies[current] == nummies[next_e]:
            nummy += nummies[current]
    return nummy
