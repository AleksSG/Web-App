$(function() {
  $("#id_group_name").autocomplete({
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
        $("#id_group_name").val(ui.item.artistName);
        $("#id_group_url").val(ui.item.artistViewUrl);
      }
    }
  });
});

$(function() {
  $("#id_song_name").autocomplete({
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
              label: item.trackName,
              value: item.trackName,
              trackName: item.trackName,
              artistName: item.artistName,
              collectionName: item.collectionName,
              releaseDate: item.releaseDate.substring(0, 10),
              primaryGenreName: item.primaryGenreName,
              trackViewUrl: item.trackViewUrl,
            }
          }));
        }
      });
    },
    minLength: 3,
    select: function( event, ui ) {
      if (ui.item) {
        $("#id_song_name").val(ui.item.trackName);
        $("#id_group").val(ui.item.artistName);
        $('#id_album').val(ui.item.collectionName);
        $('#id_releaseDate').val(ui.item.releaseDate)
        $('#id_genre').val(ui.item.primaryGenreName)
        $('#id_song_url').val(ui.item.trackViewUrl)
      }
    }
  });
});
