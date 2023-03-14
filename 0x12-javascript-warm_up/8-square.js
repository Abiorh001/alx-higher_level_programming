#!/usr/bin/node

const myVar = process.argv[2];
const num = parseInt(myVar);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    let row = '';
    for (let j = 0; j < myVar; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
