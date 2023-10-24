#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const RESULT = body;
    fs.writeFile('loripsum', RESULT, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
