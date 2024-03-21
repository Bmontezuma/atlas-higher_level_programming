#!/usr/bin/node

/**
 * Script that will  print multiple lines using an array of strings and a loop
 *
 * This script prints multiple lines by using an array of strings and a loop.
 * Each line is printed on a new line using a single console.log statement.
 *
 * Usage: ./6-multi_languages_loop.js
 */

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
}
