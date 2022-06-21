#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(0, list_length):
        try:
            new = my_list_1[i] / my_list_2[i]
        except(ZeroDivisionError):
            print("division by 0")
            new = 0
        except(TypeError):
            print("wrong Type")
            new = 0
        except(IndexError):
            print("out of range")
            new = 0
        finally:
            list.append(new)
    return list
