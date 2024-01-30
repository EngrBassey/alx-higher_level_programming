#!/usr/bin/node
// A script that reads and prints the content of a file

const file = process.argv[2];
const strFile = process.argv[3];
const fs = require('fs');

fs.writeFile(file, strFile, (error) => {
  if (error) {
    console.log(error);
  }
});
