#!/usr/bin/python3
for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        sep = ", " if units_digit < 9 else "\n"
        print("{:d}{:d}".format(tens_digit, units_digit), end=sep)
