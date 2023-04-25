#!/usr/bin/node

// a script to write data into a file

const fs = require('fs');
const url = process.argv[2];
const request = require('request');
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(process.argv[3], body, 'utf8', err => {
    if (err) {
      console.error(err);
    }
  });
});
