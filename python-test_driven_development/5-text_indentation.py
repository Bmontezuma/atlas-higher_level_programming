#!/usr/bin/python3

import doctest

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'
    
    Args:
        text (str): The input text.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    punctuation_chars = ['.', '?', ':']
    
    for char in text:
        print(char, end='')
        if char in punctuation_chars:
            print('\n')

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == "__main__":
    import unittest
    unittest.main()
