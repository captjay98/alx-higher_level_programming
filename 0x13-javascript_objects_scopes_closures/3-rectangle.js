#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const rec = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(rec.repeat(this.width));
    }
  }
};
