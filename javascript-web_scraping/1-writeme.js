#!/usr/bin/node

const fs = require('fs');

// Check if both file path and string arguments are provided
if (process.argv.length !== 4) {
  console.log('Usage: ./1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote "${stringToWrite}" to ${filePath}`);
  }
});
