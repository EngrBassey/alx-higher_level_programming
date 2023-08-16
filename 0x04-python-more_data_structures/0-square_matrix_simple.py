#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_l = []
    for i in matrix:
        new_l.append([element ** 2 for element in i])
    return(new_l)
