#!/usr/bin/node
const ArrayNum = process.argv.slice(2);
if (ArrayNum.length === 1) {
  console.log(0);
} else if (ArrayNum.length === 0) {
  console.log(0);
} else {
  ArrayNum.sort(function (a, b) {
    return b - a;
  });
  console.log(ArrayNum[1]);
}
