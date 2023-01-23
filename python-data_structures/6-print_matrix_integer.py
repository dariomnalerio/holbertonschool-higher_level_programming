#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end="")
            if i != length:
                print(end=" ")
        print()
