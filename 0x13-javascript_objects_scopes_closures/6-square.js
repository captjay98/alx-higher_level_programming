#!/usr/bin/node
const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    } else {
      this.print();
    }
  }
};

module.exports = Square;
