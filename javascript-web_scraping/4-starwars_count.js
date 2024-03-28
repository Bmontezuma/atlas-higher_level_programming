#!/usr/bin/node

const request = require('request');

// Check if API URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./4-starwars_count.js <api-url>');
  process.exit(1);
}

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = '18';

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const films = JSON.parse(body).results;
  const count = films.filter(film => film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)).length;
  console.log(count);
});
