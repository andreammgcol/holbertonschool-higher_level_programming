#!/usr/bin/node
const Argv1 = parseInt(process.argv[2]);
if (Argv1) {
  console.log('My number: ' + Argv1);
} else {
  console.log('Not a number');
}
