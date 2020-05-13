#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const apiData = JSON.parse(body);
    const films = apiData.results;
    const ID = 'https://swapi-api.hbtn.io/api/people/18/';
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === ID) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
