#!/usr/bin/node

/**
 * Function to compute the factorial of a number recursively
 * @param {number} n - The number for which to compute the factorial
 * @returns {number} The factorial of n
 */
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }
  // Recursive case: n * factorial(n - 1)
  return n * factorial(n - 1);
}

// Parse command-line argument as an integer
const num = parseInt(process.argv[2]);

// Check if the argument is provided and is a valid integer
if (!isNaN(num)) {
  // Compute and print the factorial of the number
  console.log(factorial(num));
} else {
  // Print 1 if the argument is NaN
  console.log(1);
}
