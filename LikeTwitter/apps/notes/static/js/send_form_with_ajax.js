$(document).ready(function(){
    $('form').submit(function()  {
    if ($('#id_image_of_note').val() == '') {
          var msg   = $('#add_note').serialize();
          $.ajax({
            type: 'POST',
            url: 'notes/',
            data: msg,
            success: function(data) {
                $('.row').last().after(data);
            },
            error:  function(xhr, str){
                alert('Exception ' + xhr.responseCode);
            }
          });
          return false;
       } 
    });
});