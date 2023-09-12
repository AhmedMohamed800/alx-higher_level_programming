#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((e) => { return e === searchElement; }).length;
};
