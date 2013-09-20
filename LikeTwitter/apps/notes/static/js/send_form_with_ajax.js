$(document).ready(function(){
  $('form').submit(function()  {
    $('[errors=errors]').remove()
    if ($('#id_image_of_note').val() == '') {
      var msg = $('#add_note').serialize();
      $.ajax({
        type: 'POST',
        url: '',
        data: msg,
        success: function(data) {
          if (data.indexOf("errors") !=-1) {
            $('#id_body').after(data);
          }
          else {
            document.location = '/';
            }
        },
        error:  function(xhr, str){
          document.location = 'add_note_with_ajax/';
          alert('Except' + xhr.responseCode);
        }
      });
      return false;
    } 
  });
});