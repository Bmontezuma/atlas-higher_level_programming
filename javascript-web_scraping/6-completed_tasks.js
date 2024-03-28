#!/usr/bin/node

const request = require('request');

// Check if API URL argument is provided
if (process.argv.length !== 3) {
  console.log('Usage: ./6-completed_tasks.js <api-url>');
  process.exit(1);
}

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  // Count the number of completed tasks for each user
  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
