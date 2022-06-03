#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    answer = 0

    x = (len(sys.argv) - 1)
    q = sys.argv[2]

    operators = ["+", "-", "*", "/"]

    if x < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> \n")
        sys.exit(1)

    if sys.argv[2] not in operators:
        print("Unknown operator.Available operators: +, -, * and /\n")
        sys.exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if q == operators[0]:
            print("{} {} {} = {}".format(a, operators[0], b, add(a, b)))

        if q == operators[1]:
            print("{} {} {} = {}".format(a, operators[1], b, sub(a, b)))

        if q == operators[2]:
            print("{} {} {} = {}".format(a, operators[2], b, mul(a, b)))

        if q == operators[3]:
            print("{} {} {} = {}".format(a, operators[3], b, div(a, b)))
