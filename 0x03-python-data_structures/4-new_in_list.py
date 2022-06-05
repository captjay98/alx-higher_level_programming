#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new = my_list.copy()
        new = my_list.remove(idx + 1)
        new = my_list.insert(idx, element)
        return new
