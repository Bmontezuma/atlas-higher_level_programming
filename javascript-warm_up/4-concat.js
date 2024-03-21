#!/usr/bin/node

/**
 * Script that will print two arguments passed to it in a specific format
 *
 * This script prints two arguments passed to it in the following format:
 *  - If both arguments are passed, it prints "<arg1> is <arg2>"
 *  - If only one argument is passed, it prints "<arg1> is undefined"
 *  - If no arguments are passed, it prints "undefined is undefined"
 *
 * Usage: ./4-concat.js [arg1] [arg2]
 */

const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

console.log(`${arg1} is ${arg2}`);
