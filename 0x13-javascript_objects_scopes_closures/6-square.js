#!/usr/bin/node

const SquareF = require('./5-square');

module.exports = class Square extends SquareF {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let itemOb = '';
      for (let j = 0; j < this.width; j++) {
        itemOb += c;
      }
      console.log(itemOb);
    }
  }
};
