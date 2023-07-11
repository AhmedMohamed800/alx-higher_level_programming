#!/usr/bin/python3
"""Student Class"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if attr is None:
            return self.__dict__
        dicty = {}
        for ele in attr:
            if ele in self.__dict__.keys():
                dicty[ele] = self.__dict__[ele]
        return dicty

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
