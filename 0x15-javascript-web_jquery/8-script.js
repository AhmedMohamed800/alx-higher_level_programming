$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (data) {
    for (const element of data.results) {
      $('UL#list_movies').append(`<li>${element.title}</li>`);
    }
  },
  error: function (error) {
    console.error(error);
  }
});
