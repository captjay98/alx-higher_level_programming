#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = number % 10 if number >= 0 else -number % 10

    print(lastDigit)

    return lastDigit


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
