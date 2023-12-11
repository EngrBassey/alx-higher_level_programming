#!/usr/bin/node

const args = process.argv;

if (args.length === 2) {
  console.log('Missing number of occurrences');
}
for (let i = 1; i <= parseInt(args[2]); i++) {
  console.log('C is fun');
}
