#!/usr/bin/node

// a script to get status code from api get request

const request = require('request');
request(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
