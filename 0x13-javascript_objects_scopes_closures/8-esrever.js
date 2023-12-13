#!/usr/bin/node

exports.esrever = function (list) {
  const item = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    item[j] = list[i];
    j++;
  }
  return item;
};
