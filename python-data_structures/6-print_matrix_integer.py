#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for row in matrix:
        for i in row:
            if i == row[-1]:
                print("{}".format(i))
            else:
                print("{}".format(i), end=' ')
