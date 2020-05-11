#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    this.height ^= this.width;
    this.width ^= this.height;
    this.height ^= this.width;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
