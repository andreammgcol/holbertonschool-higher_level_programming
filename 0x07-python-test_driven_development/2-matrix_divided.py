#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for element in matrix:
        if type(element) != int and type(element) != float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        