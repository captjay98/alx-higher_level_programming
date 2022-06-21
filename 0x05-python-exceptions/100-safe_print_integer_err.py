#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    x = value

    try:
        print("{:d}".format(x))
        return True
    except ValueError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    except TypeError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
