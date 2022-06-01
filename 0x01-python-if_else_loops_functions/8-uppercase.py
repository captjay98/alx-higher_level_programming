#!/usr/bin/python3

def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        return(ord(str) - 32)
    else:
        return ord(str)
