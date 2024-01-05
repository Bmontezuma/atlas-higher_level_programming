#!/usr/bin/python3

def print_last_digit(number):
    if isinstance(number, int):
        last_digit = abs(number) % 10
        print(last_digit, end="")
        return last_digit
    else:
        raise TypeError("Input must be an integer")
