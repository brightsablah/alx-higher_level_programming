#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix.copy()
    for row in copy:
        for num in row:
            num *= num
    return copy
