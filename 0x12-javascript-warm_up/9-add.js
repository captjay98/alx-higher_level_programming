#!/usr/bin/node

const args = process.argv;

const add = function (a, b) {
  return a + b;
};
const answer = add(parseInt(args[2]), parseInt(args[3]));
console.log(answer);
