#!/usr/bin/node

/**
 * Script to print a message depending on the number of arguments passed
 *
 * This script prints different messages based on the number of arguments passed:
 *  - If no arguments are passed, it prints "No argument"
 *  - If only one argument is passed, it prints "Argument found"
 *  - If more than one argument is passed, it prints "Arguments found"
 *
 * Usage: ./2-arguments.js [args...]
 */

const argsLength = process.argv.length;

if (argsLength === 2) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
