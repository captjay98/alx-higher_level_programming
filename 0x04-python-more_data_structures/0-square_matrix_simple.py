#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for num in matrix:
        new_matrix.append(list(map(lambda num: num**2, num)))

    return new_matrix




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))
