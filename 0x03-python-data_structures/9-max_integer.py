#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    largest = my_list[0]

    for item in range(len(my_list)):
        if my_list[item] > largest:
            largest = my_list[item]

    return largest
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
