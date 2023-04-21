#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const movie of movies) { // for each movie
      for (const character of movie.characters) { // for each character in the movie
        if (character.includes(characterId)) { // if the character id is 18
          count++;
        }
      }
    }
    console.log(count);
  }
});
