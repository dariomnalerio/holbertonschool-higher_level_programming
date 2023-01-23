#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = []
    for i in range(len(matrix)):
        num = list(map(lambda x: x ** 2, matrix[i]))
        new_matrix.append(num)
    return new_matrix
