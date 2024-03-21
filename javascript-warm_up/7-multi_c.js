#!/usr/bin/node

/**
 * Script that will print "C is fun" x times
 *
 * This script prints "C is fun" x times, where x is the first argument of the script.
 * If the first argument can't be converted to an integer, it prints "Missing number of occurrences".
 *
 * Usage: ./7-multi_c.js [x]
 */

const x = parseInt(process.argv[2]);

if (!Number.isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
