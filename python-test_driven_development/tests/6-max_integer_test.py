#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([-1, -3, -4, -2], -1),
        ([], None),
        ([-1], -1),
        ([0, 0, 0, 0], 0),
        ([5, 5, 5, 5, 5, 5], 5),
        ([1, 2, 3, 4, 5, 0], 5),
        ([-5, -4, -3, -2, -1], -1),
        ([1, 2, 3, 4, 5], 5),  # Test case: Max at the end
        ([5, 1, 2, 3, 4], 5),  # Test case: Max at the beginning
        ([1, 2, 5, 3, 4], 5),  # Test case: Max in the middle
        ([-1, 2, 3, 4], 4),    # Test case: One negative number in the list
        ([-1, -2, -3, -4], -1),  # Test case: Only negative numbers in the list
        ([5], 5),              # Test case: List of one element
        ([], None),            # Test case: List is empty
    ])
    def test_max_integer(self, input_list, expected_result):
        """Test max_integer function with various input lists"""
        result = max_integer(input_list)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
