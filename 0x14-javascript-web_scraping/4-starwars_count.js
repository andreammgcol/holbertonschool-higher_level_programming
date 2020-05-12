#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const apiData = JSON.parse(body);
    // console.log(data.title);
    // console.log(JSON.parse(body).title);

    const films = apiData.results;
    for (let i = 0; i < films.length; i++) {
       const characters = films[i].characters
       for (let j = 0;  j < characters.length; j++){
         console.log(`personaje: ${characters[j]}`);
       }      
    }
  }
});
