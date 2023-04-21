#!/usr/bin/node
// Class Rectangle that defines a rectangle

class Rectangle {
  // Constructor that defines the width and the height of the rectangle
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Print the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchange the width and the height of the rectangle
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    // Multiply the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
