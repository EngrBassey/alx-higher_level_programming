#!/usr/bin/node

const args = process.argv;
const processArgs = args.length;

if (processArgs === 2) {
  console.log('No argument');
} else if (processArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
