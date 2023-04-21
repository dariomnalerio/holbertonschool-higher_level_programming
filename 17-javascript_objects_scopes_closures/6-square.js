#!/usr/bin/node
// Class Square that defines a square and inherits from Rectangle

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    // Print square using the character c or X if c is undefined
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
