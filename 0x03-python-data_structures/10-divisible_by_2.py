#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for ele in range(len(my_list)):
        if new_list[ele] % 2 == 0:
            new_list[ele] = True
        else:
            new_list[ele] = False
    return new_list
