#!/usr/bin/node

/**
 * Script that prints the first argument passed to it
 *
 * This script prints the first argument passed to it:
 *  - If no arguments are passed, it prints "No argument"
 *  - Otherwise, it prints the first argument
 *
 * Usage: ./3-value_argument.js [args...]
 */

const arg = process.argv[2];

if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
