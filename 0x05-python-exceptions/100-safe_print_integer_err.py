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
    
    
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
