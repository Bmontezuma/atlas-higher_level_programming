#!/usr/bin/python3
import random
# This will assign a random number to 'number'
number = random.randint(-10, 10)

# Print assigned number.
print("The number:", number)

# Check if number is positive, negative, or a zero.
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
