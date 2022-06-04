#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for item in my_list:
        print("{:d}".format(item))


print(print_list_integer([5, 6, 7, 8]))
