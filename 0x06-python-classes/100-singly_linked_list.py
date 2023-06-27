#!/usr/bin/python3
"""Linked list in python"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        if next_node is None:
            self.__next_node = next_node
        elif not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        elif not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value, None)
        current = self.__head
        if self.__head is None:
            self.__head = new
            return
        while current is not None:
            if current is self.__head and value < current.data:
                self.__head = new
                new.next_node = current
                return
            elif current.next_node is None and value > current.data:
                current.next_node = new
                return
            elif value < current.data:
                new.data = current.data
                current.data = value
                new.next_node = current.next_node
                current.next_node = new
                return
            current = current.next_node
        return

    def __str__(self):
        st = ""
        current = self.__head

        while current:
            st += str(current.data) + '\n'
            current = current.next_node
        return st[: -1]
