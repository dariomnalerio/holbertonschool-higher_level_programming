#!/usr/bin/node
// Script that replaces the value 12 with 89 in an object

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.value = 89;

console.log(myObject);
