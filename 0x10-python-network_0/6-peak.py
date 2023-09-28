#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    merge_sort(list_of_integers, 0, length - 1)
    return list_of_integers[length - 1]


def merge(list_of_integers, left, middle, right):
    """merge sort"""
    arr1 = middle - left + 1
    arr2 = right - middle

    Left = [0] * (arr1)
    Right = [0] * (arr2)

    for i in range(0, arr1):
        Left[i] = list_of_integers[left + i]

    for j in range(0, arr2):
        Right[j] = list_of_integers[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < arr1 and j < arr2:
        if Left[i] <= Right[j]:
            list_of_integers[k] = Left[i]
            i += 1
        else:
            list_of_integers[k] = Right[j]
            j += 1
        k += 1

    while i < arr1:
        list_of_integers[k] = Left[i]
        i += 1
        k += 1

    while j < arr2:
        list_of_integers[k] = Right[j]
        j += 1
        k += 1


def merge_sort(list_of_integers, left, right):
    """conquer the list"""
    if left < right:
        middle = left + (right - left) // 2
        merge_sort(list_of_integers, left, middle)
        merge_sort(list_of_integers, middle + 1, right)
        merge(list_of_integers, left, middle, right)
