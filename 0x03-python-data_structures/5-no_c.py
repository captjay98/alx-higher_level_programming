#!/usr/bin/python3

def no_c(my_string):
    copy = my_string.translate({ord(c): None for c in "c C"})

    return copy
