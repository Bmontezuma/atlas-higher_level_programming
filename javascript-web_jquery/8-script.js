$(document).ready(function() {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    const movies = data.results;

    movies.forEach(function(movie) {
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
