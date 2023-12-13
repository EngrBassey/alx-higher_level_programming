#!/usr/bin/node

const dict = require('./101-data');

const newDict = {};
const entries = dict.dict;

for (const key in entries) {
  if (newDict[entries[key]] === undefined) {
    newDict[entries[key]] = [key];
  } else {
    newDict[entries[key]].push(key);
  }
}

console.log(newDict);
