#!/usr/bin/python3
"""Module of pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing"""
    x = [[1], [1, 1], [1, 2, 1]]
    if n <= 0:
        return []
    if n == 1:
        return [1]
    elif n == 2:
        return [[1], [1, 1]]
    elif n == 3:
        return x
    new_list = []
    for i in range(n - 3):
        for j in range(len(x[-1])):
            if j == 0:
                new_list.append(x[-1][j])
                new_list.append(x[-1][j] + x[-1][j + 1])
                continue
            elif j == len(x[-1]) - 1:
                new_list.append(x[-1][j])
                break
            new_list.append(x[-1][j] + x[-1][j + 1])
        x.append(new_list)
        new_list = []
    return x


print(pascal_triangle(20))
