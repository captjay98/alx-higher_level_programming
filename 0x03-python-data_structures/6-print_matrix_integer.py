#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print("{:d}".format(matrix[row][column]), end=" ")
            if column != (len(matrix[row]) - 1):
                    print(" ", end =" ")
        print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()