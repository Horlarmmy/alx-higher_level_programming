#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for list in matrix:
            for i in range(len(list)):
                if i != len(list) -1:
                    print(list[i],end="")
                else:
                    print(list[i])
