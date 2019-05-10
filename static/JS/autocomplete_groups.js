$(function() {
  $("#inputGroupName").autocomplete({
    source: function(request, response) {
      $.ajax({
        url: "https://itunes.apple.com/search",
        dataType: "jsonp",
        data: {
          entity: "song",
          term: request.term
        },
        success: function ( data ) {
          response( $.map( data.results, function(item) {
            return {
              label: item.artistName,
              value: item.artistName,
              artistName: item.artistName,
              artistViewUrl: item.artistViewUrl
            }
          }));
        }
      });
    },
    minLength: 3,
    select: function( event, ui ) {
      if (ui.item) {
        $("#inputGroupName").val(ui.item.artistName);
        $("#inputGroupUrl").val(ui.item.artistViewUrl);
      }
    }
  });
});
