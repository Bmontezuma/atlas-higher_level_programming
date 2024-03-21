#!/usr/bin/node

/**
 * Script that will print the first argument as an integer if possible
 *
 * This script prints "My number: <first argument converted to an integer>"
 * if the first argument can be converted to an integer.
 * If the argument can't be converted to an integer, it prints "Not a number".
 *
 * Usage: ./5-to_integer.js [arg]
 */

const arg = process.argv[2];

if (Number.isInteger(parseInt(arg))) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
