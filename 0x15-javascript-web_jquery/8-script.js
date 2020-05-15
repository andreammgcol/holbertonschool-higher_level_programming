$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films) {
  $.each(films.results, function (data, movies) {
    $('#list_movies').append('<li>' + movies.title + '</li>');
  });
}, 'json'
);
