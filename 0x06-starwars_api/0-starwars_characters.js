#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Send a request to the Star Wars API to fetch information about the film with the specified ID
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  // Handle errors
  if (err) throw err;

  // Parse the response body to extract the list of actors in the film
  const actors = JSON.parse(body).characters;

  // Call the function to print the names of the actors in the exact order they appear in the film
  printActorsInOrder(actors, 0);
});

// Function to print the names of the actors in the exact order they appear in the film
const printActorsInOrder = (actors, index) => {
  // Base case: If all actors have been printed, return
  if (index === actors.length) return;

  // Send a request to fetch information about the actor at the current index
  request(actors[index], function (err, res, body) {
    // Handle errors
    if (err) throw err;

    // Parse the response body to extract the name of the actor
    const actorName = JSON.parse(body).name;

    // Print the name of the actor
    console.log(actorName);

    // Recursively call the function to print the next actor in the list
    printActorsInOrder(actors, index + 1);
  });
};
