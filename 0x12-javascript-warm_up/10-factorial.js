#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const firstArg = parseInt(process.argv[2]);
if (firstArg) {
  console.log(factorial(firstArg));
} else {
  console.log(1);
}
