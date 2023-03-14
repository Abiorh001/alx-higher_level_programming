#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const result = factorial(num);
console.log(result);
