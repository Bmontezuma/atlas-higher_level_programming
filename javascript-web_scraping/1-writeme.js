#!/usr/bin/node

const fs = require('fs').promises;

// Check if correct number of arguments are passed
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Extract arguments
const [, , filePath, content] = process.argv;

// Write content to file
async function writeToFile () {
  try {
    await fs.writeFile(filePath, content, { encoding: 'utf-8' });
    const data = await fs.readFile(filePath, { encoding: 'utf-8' });
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

writeToFile();
