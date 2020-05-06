#!/usr/bin/node
function factorialRecursivo (n) {
  let result;
  if (n === 0) {
    return 1;
  } else {
    result = n * factorialRecursivo(n - 1);
  }
  return result;
}
const n = parseInt(process.argv[2]);
console.log(factorialRecursivo(n));
