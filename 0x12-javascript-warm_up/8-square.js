#!/usr/bin/node

const args = process.argv;

if (args[2] && parseInt(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('x'.repeat(parseInt(args[2])));
  }
} else {
  console.log('Missing size');
}
