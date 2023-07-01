#!/usr/bin/python3
"""Module for text_indentation"""


def text_indentation(text):
    """
     prints a text with 2 new lines after each of these characters: ., ? and :

     Arguments:
        text: text to use (str)

    Returns:
        Nothing
    """
    stringy = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] not in [":", ".", "?"]:
            stringy += text[i]
        else:
            stringy += text[i]
            print("{}".format(stringy.strip()))
            print()
            stringy = ""
