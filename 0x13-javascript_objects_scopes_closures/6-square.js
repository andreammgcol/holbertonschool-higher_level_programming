#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charPrint;
    if (c && typeof c === 'string') {
      charPrint = c;
    } else {
      charPrint = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write(charPrint);
      }
      console.log();
    }
  }
}
module.exports = Square;
