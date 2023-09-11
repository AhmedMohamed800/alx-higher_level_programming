#!/usr/bin/node

const args = process.argv;
let message = 'No argument';

if (args[2]) {
  message = args[2];
}

console.log(message);
