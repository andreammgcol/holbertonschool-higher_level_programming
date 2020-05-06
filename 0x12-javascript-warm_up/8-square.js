#!/usr/bin/node
const sizeSquare = parseInt(process.argv[2]);
if (sizeSquare) {
  for (let row = 0; row < sizeSquare; row++) {
    for (let column = 0; column < sizeSquare; column++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
