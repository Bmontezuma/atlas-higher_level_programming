const fs = require('fs');

// Check if correct number of arguments are passed
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Extract arguments
const [, , filePath, content] = process.argv;

// Write content to file
fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content); // Output the content directly
});
