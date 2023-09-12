#!/usr/bin/node

exports.esrever = function (list) {
  let iReversed = list.length - 1;
  const newList = list;
  for (let i = 0; i < list.length; i++) {
    if (iReversed === i || i > iReversed) {
      break;
    }
    [newList[i], newList[iReversed]] = [newList[iReversed], newList[i]];
    --iReversed;
  }
  return newList;
};
