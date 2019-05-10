var $radios = $("input[name='model']");
$radios.change(function() {
  var checked = $radios.filter(':checked').val();
  if (checked == 'group') {
    $('#add_group').slideDown(1000);
  } else {
    $('#add_group').slideUp(1000);
  }
  if (checked == 'song') {
    $('#add_song').slideDown(1000);
  } else {
    $('#add_song').slideUp(1000);
  }
});
