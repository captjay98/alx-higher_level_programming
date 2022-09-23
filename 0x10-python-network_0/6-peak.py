#!/usr/bin/python3
"""
    finds a peak in a list of unsorted integers
"""


def find_peak(num):
    '''
        Finds the peak in a list of numbers
    '''

    length = len(num)
    if length == 0:
        return None
    if length == 1:
        return (num[0])
    if length == 2:
        return max(num)

    for n in range(0, length):
        value = num[n]
        if (n > 0 and n < length - 1 and
                num[n + 1] <= value and num[n - 1] <= value):
                return value
        elif n == 0 and num[n + 1] <= value:
            return value
        elif n == length - 1 and num[n - 1] <= value:
            return value
    return value
