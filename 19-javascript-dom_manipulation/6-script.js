#!/usr/bin/node
// Script that fetches the character name

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((response) => response.json()) // Converts the response to JSON
  .then((data) => { // data is the JSON object
    const name = data.name; // Gets the name from the JSON object
    document.querySelector('#character').innerHTML = name; // Sets the innerHTML of the element with id character to the name
  });
