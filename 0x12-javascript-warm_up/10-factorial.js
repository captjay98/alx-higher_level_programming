#!/usr/bin/node

const args = process.argv;

const fact = function (x) {
  if (isNaN(x) || x === 1) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
};
const answer = fact(parseInt(args[2]));
console.log(answer);
