#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // get arguments and convert to numbers
const n = args.length;

if (n === 0) {
  console.log(0);
} else if (n === 1) {
  console.log(0);
} else {
  let biggest = args[0];
  let secondBiggest = -Infinity;

  for (let i = 1; i < n; i++) {
    const x = args[i];
    if (x > biggest) {
      secondBiggest = biggest;
      biggest = x;
    } else if (x > secondBiggest && x !== biggest) {
      secondBiggest = x;
    }
  }

  console.log(secondBiggest);
}
