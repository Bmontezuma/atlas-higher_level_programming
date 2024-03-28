#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
