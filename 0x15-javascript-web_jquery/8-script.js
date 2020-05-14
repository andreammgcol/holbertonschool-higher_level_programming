$.get('https://swapi.co/api/films/?format=json', function (films) {
  $.each(films.results, function (data, movies) {
    $('#list_movies').append('<li>' + movies.title + '</li>');
  });
}, 'json'
);
