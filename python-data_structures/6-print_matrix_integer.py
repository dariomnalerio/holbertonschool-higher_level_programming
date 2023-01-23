#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end="")
            if i != length:
                print(end=" ")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()