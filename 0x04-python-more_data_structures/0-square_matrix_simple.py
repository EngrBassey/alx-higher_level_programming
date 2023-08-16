#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_l = [[element ** 2 for element in row] for row in matrix]
    return(new_l)
