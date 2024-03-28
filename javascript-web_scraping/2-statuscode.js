#!/usr/bin/node

const request = require('request');

// Check if URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

// Get the URL from command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
