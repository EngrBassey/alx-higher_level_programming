$(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
      const films = data.results;
      films.forEach(films => {
        $('#list_movies').append('<li>' + films.title + '</li>')
      });
    }
  });
});
