#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for i in row:
            if i == row[-1]:
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end=' ')
