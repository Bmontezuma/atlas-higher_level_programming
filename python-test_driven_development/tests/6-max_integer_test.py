# Test case: Normal case with positive integers
>>> max_integer([1, 2, 3, 4])
4

# Test case: Normal case with positive integers in a different order
>>> max_integer([1, 3, 4, 2])
4

# Test case: Normal case with negative integers
>>> max_integer([-1, -3, -4, -2])
-1

# Test case: Empty list
>>> max_integer([])
None

# Test case: List with a single negative integer
>>> max_integer([-1])
-1

# Test case: List with all zeros
>>> max_integer([0, 0, 0, 0])
0

# Test case: List with all the same positive integer
>>> max_integer([5, 5, 5, 5, 5, 5])
5

# Test case: List with a mix of positive and zero
>>> max_integer([1, 2, 3, 4, 5, 0])
5

# Test case: List with all negative integers
>>> max_integer([-5, -4, -3, -2, -1])
-1
