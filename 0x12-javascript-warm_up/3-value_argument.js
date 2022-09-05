#!/usr/bin/node

const args = process.argv;

if (args === 2) {
  console.log('No argument');
} if (args[2]) {
  console.log(`${args[2]}`);
}
args.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});