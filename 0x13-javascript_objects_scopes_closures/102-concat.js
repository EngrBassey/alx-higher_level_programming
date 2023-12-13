#!/usr/bin/node

const fs = require('fs');
const filA = process.argv[2];
const fileB = process.argv[3];

const readA = fs.readFileSync(filA);
const readB = fs.readFileSync(fileB);

const readC = readA + readB;

fs.writeFile(process.argv[4], readC, 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
