#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0

    avgr = 0
    size = 0
    answr = 0

    for x, y in my_list:
        avgr += x * y
        size += y
        answr = avgr / size
    return answr
