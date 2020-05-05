#!/usr/bin/node
let myArgs = process.argv.slice(1);
if (myArgs.length < 2) {
    console.log('No argument');
} else {
    console.log('Argument found')
}
