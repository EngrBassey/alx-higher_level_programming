#!/usr/bin/node
const args = process.argv;

if (args.length === 2 || isNaN(args[2])) {
  console.log('Missing size');
} for (let i = 1; i <= parseInt(args[2]); i++) {
  let items1 = '';
  for (let i = 1; i <= parseInt(args[2]); i++) {
    items1 += 'X';
  }
  console.log(items1);
}
