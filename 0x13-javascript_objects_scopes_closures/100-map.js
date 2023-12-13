#!/usr/bin/node

const list = require('./100-data').list;

const modifiyArr = list.map(function (element, index) {
  return (element * index);
});
console.log(list);
console.log(modifiyArr);
