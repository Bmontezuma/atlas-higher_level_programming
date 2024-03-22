#!/usr/bin/node

/**
 * Function to add two integers
 * @param {number} a - The first integer
 * @param {number} b - The second integer
 * @returns {number} The addition of a and b
 */
function add (a, b) {
  return a + b;
}

// Parse command-line arguments as integers
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are provided and are valid integers
if (!isNaN(num1) && !isNaN(num2)) {
  // Print the addition of the two integers
  console.log(add(num1, num2));
} else {
  // Print "NaN" if either argument is missing or invalid
  console.log('NaN');
}
