#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 * Usage: ./0-starwars_characters.js [film_id]
 *
 * Description:
 * * Fetch a starwars movie based on the passed ID and display one character name
 * * per line in the same order as the “characters” list in the /films/ endpoint
 */

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

const url = 'https://swapi-api.alx-tools.com/api/films/';

async function getStarwarsCharacters (id) {
  if (!id || isNaN(+id) || +id < 1) {
    console.log('Usage: ./0-starwars_characters.js [film_id]');
    return;
  }

  try {
    const response = await requestPromise(url + id);
    const characters = JSON.parse(response.body).characters;

    for (const characterUrl of characters) {
      const response = await requestPromise(characterUrl);
      console.log(JSON.parse(response.body).name);
    }
  } catch (err) {
    console.log(err);
  }
}

const id = process.argv[2];
getStarwarsCharacters(id);
