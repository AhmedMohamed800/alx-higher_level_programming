#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        for listy in matrix:
            for num in range(len(listy)):
                if listy[num] != listy[-1]:
                    print("{:d}".format(listy[num]), end=" ")
                else:
                    print("{:d}".format(listy[num]))
    else:
        print()
