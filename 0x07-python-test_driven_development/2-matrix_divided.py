#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    ty_err = "matrix must be a matrix (list of lists) of integers/floats"
    le_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(ty_err)

    for r in range(len(matrix)):
        if type(matrix[r]) != list:
            raise TypeError(ty_err)

    for r in range(len(matrix)):
        if matrix[r] == []:
            raise TypeError(ty_err)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if type(matrix[r][c]) != int and type(matrix[r][c]) != float:
                raise TypeError(le_err)

    for row in range(len(matrix)):
        if row > 0:
            if len(matrix[row]) != len(matrix[row - 1]):
                raise TypeError(row_err)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = copy_matrix(matrix)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new_element = matrix[row][column]
            new_element = new_element / div
            new_element = round(new_element, 2)
            new_matrix[row][column] = new_element

    return new_matrix


def copy_matrix(realMatrix):
    return [list(element) for element in realMatrix]
