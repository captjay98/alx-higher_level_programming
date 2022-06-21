#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []

    for i in range(list_length):
        try:
            new = my_list_1[i] / my_list_2[i]

        except(ZeroDivisionError):
            print("division by 0")
            continue

        except(TypeError):
            print("wrong Type")
            continue

        except(IndexError):
            print("Out of range")
            continue

        finally:
            list.append(new)
    return list
