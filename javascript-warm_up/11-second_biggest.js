#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort();
  console.log(sortedArgs[sortedArgs.length - 2]);
}
