#!/usr/bin/node

const request = require('request');

// Check if movie ID argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./3-starwars_title.js <movie-id>');
  process.exit(1);
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Make a GET request to the Star Wars API endpoint
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movieDetails = JSON.parse(body);
  console.log(movieDetails.title);
});
