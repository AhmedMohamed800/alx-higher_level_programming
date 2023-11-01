$('DIV#add_item').on('click', function () {
  const ITEM = $('<li>', {
    text: 'item'
  });
  $('UL.my_list').append(ITEM);
});
