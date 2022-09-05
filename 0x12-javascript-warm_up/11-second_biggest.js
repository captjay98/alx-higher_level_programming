#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log(0);
} else if (args[2] === 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > args[i + 1]) {
      console.log(args[i]);
    }
  }
}
