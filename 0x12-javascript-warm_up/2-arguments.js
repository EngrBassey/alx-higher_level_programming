#!/usr/bin/node

const process = require('process');
const args = process.argv;
const processArgs = args.length;

if (processArgs === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
