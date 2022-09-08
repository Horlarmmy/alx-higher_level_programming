#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const s = searchElement;
  let count = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === s) {
      count++;
    }
  }
  return count;
};
