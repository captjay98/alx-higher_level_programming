#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for value in new_dict.keys():
        new_dict[value] *= 2
    print(new_dict)
    return new_dict
