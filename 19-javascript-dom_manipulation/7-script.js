#!/usr/bin/node
// Script that fetches and lists the title for all movies

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((response) => response.json()) // Converts the response to JSON
  .then((data) => { // data is the JSON object
    const movies = data.results; // Gets the results from the JSON object
    for (const movie of movies) { // Loops through the movies
      const li = document.createElement('li'); // Creates a new li element
      document.querySelector('ul#list_movies').appendChild(li).innerHTML = movie.title;
    }
  }
  );
