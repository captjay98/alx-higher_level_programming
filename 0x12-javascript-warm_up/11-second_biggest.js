#!/usr/bin/node

const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
}
const myarr = [];

args.forEach((val) => {
  if (isNaN(val) === false) {
    myarr.push(val);
  }
});

console.log(myarr);
let largest = myarr[1];
let slargest = myarr[2];

for (let i = 0; i < myarr.length; i++) {
  if (myarr[i] > largest) {
    slargest = largest;
    largest = myarr[i];
  } else if (myarr[i] > slargest && myarr[i] < largest) {
    slargest = myarr[i];
  }
}
console.log(slargest);
