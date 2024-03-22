#!/usr/bin/node

/**
 * Function to find the second biggest integer in a list of numbers
 * @param {number[]} numbers - The list of numbers
 * @returns {number} The second biggest integer in the list
 */
function secondBiggest (numbers) {
  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);

  // Return the second element if it exists, otherwise 0
  return numbers[1] || 0;
}

// Parse command-line arguments as integers
const args = process.argv.slice(2).map(Number);

// Check if no arguments or only one argument is provided
if (args.length < 2) {
  console.log(0);
} else {
  // Replace the value 12 with 89
  for (let i = 0; i < args.length; i++) {
    if (args[i] === 12) {
      args[i] = 89;
      break;
    }
  }

  // Print the second biggest integer in the list of arguments
  console.log(secondBiggest(args));
}
