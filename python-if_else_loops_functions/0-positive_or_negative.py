#!/usr/bin/python3
import random
# This will assign a random number to 'number'
number = random.randint(-10, 10)

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
