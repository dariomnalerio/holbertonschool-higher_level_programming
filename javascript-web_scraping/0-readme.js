#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs') // import fs module

const file = process.argv[2]; // get file name from command line

// read file and print content
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
