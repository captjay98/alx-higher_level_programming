#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0

    x = (len(sys.argv) - 1)

    for i in range(x):
        sum += int(sys.argv[i + 1])
    print(f"{sum}")
