#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    for key in a_dictionary:
        count += 1

    return count

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
