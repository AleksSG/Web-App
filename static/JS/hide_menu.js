var $radios = $("input[name='model']");
$radios.change(function() {
  var checked = $radios.filter(':checked').val();
  if (checked == 'group') {
    $('#add_group').slideDown(1000);
    $("#id_group_name }}").attr('required', true);
    $("#id_group_url }}").attr('required', true);
  } else {
    $('#add_group').slideUp(1000);
    $("#id_group_name }}").attr('required', false);
    $("#id_group_url }}").attr('required', false);
  }
  if (checked == 'song') {
    $('#add_song').slideDown(1000);
    $("#id_song_name }}").attr('required', true);
    $("#id_group_name }}").attr('required', true);
    $("#id_album }}").attr('required', true);
    $("#id_releaseDate }}").attr('required', true);
    $("#id_genre }}").attr('required', true);
    $("#id_song_url }}").attr('required', true);

  } else {
    $('#add_song').slideUp(1000);
    $("#id_song_name }}").attr('required', false);
    $("#id_group_name }}").attr('required', false);
    $("#id_album }}").attr('required', false);
    $("#id_releaseDate }}").attr('required', false);
    $("#id_genre }}").attr('required', false);
    $("#id_song_url }}").attr('required', false);
  }
});
