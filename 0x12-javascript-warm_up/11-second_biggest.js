#!/usr/bin/node

const args = process.argv;

let largest = 0;
const myarr = [];

if (args[2] < 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      largest = args[i];
      myarr.push(largest);
    }
  }
  console.log(myarr[0]);
}
