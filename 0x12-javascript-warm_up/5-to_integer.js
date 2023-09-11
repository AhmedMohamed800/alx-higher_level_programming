#!/usr/bin/node

const args = process.argv;

if (args[2]) {
  if (parseInt(args[2])) {
    console.log(`My number is: ${parseInt(args[2])}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
