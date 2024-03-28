#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if URL and file path arguments are provided
if (process.argv.length !== 4) {
  console.log('Usage: ./5-request_store.js <url> <file-path>');
  process.exit(1);
}

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    console.log(`Data written to ${filePath}`);
  });
});
