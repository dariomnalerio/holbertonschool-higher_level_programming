#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed

const args = process.argv.length - 2; // -2 because the first two arguments are the path to the node executable and the path to the script

if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
