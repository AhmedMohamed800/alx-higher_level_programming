#!/usr/bin/node

const args = process.argv.length;
let message = '';

if (args === 2) {
  message = 'No argument';
} else if (args === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
