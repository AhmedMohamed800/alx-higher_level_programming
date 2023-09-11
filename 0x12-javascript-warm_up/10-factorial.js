#!/usr/bin/node

const factorial = (num) => {
  let result = 1;
  for (let i = 1; i < num + 1; i++) {
    result *= i;
  }
  return result;
};

const firstArg = parseInt(process.argv[2]);

console.log(factorial(firstArg));
