#!/usr/bin/node

// Function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  return list.filter((element) => element === searchElement).length; // Filter the list and return the length of the filtered list
};
