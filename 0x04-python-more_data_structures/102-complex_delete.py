#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary.values() is None:
        return None

    for key, val in a_dictionary.items():
        if val == value:
            del a_dictionary[key]
            break

    return a_dictionary
