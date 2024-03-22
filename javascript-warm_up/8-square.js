#!/usr/bin/node

/**
 * Script to print a square of a given size
 *
 * This script prints a square of a given size where the size is specified
 * as the first argument of the script.
 * It uses the character 'X' to print the square.
 *
 * Usage: ./8-square.js [size]
 */

const size = parseInt(process.argv[2]);

if (!Number.isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
