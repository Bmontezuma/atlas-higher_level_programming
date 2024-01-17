#!/usr/bin/python3
"""
Unittests for max_integer function
"""


import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):

    # Test case 1
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    # Test case 2
    def test_unsorted_numbers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    # Test case 3
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    # Add more test cases as needed
    # ...

if __name__ == '__main__':
    unittest.main()
