#!/usr/bin/node

const args = process.argv;

function factoria (num) {
  if (num === 0) {
    return (1);
  } else if (isNaN(num)) {
    return 1;
  } else {
    return num * factoria(num - 1);
  }
}

const val = factoria(parseInt(args[2]));
console.log(val);
