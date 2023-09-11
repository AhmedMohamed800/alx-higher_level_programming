#!/usr/bin/node

const args = process.argv;
args.shift();
args.shift();
const newArr = args.map((e) => { return parseInt(e); });
newArr.sort((a, b) => { return b - a; });

if (newArr.length === 0 || newArr.length === 1) {
  console.log(0);
} else {
  console.log(newArr[1]);
}
