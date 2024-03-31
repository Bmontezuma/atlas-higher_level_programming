#!/usr/bin/node

// Import 'fs' module for file manipulation
const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length < 4) {
  console.error('Usage: node writeToFile.js <filePath> <string>');
  process.exit(1);
}

// Destructure filePath and string from the arguments
const [, , filePath, string] = process.argv;

// Attempt to write the string to the file
fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.error('Error writing to file:', err);
  }
});
