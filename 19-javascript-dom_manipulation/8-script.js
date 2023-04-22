#!/usr/bin/node
// Script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML element with id hello.

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    document.querySelector('#hello').innerHTML = data.hello;
  }
  );
