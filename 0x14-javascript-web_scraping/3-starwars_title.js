#!/usr/bin/node

// a script to get status code from api get request

const request = require('request');
const urlpath = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(urlpath, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
