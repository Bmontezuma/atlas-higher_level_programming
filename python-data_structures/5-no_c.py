#!/usr/bin/python3
def no_c(my_string):
    new_chars = [char for char in my_string if char.lower() not in {'c', 'C'}]
    return ''.join(new_chars)
