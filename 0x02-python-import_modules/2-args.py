#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    x = len(sys.argv) - 1

    if x == 0:
        print("{:d} arguments.".format(x))
    if x == 1:
        print(f"{x} argument:")
    if x >= 2:
        print(f"{x} arguments:")

    for i in range(x):
        print(f"{i + 1}: {sys.argv[i+1]}")
