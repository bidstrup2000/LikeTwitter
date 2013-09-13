$(document).ready(function(){
  $('form').submit(function()  {
    $('[errors=errors]').remove()
    if ($('#id_image_of_note').val() == '') {
      var msg   = $('#add_note').serialize();
      $.ajax({
        type: 'POST',
        url: 'notes/',
        data: msg,
        success: function(data) {
            if (data.indexOf("errors") !=-1) {
              $('#id_body').before(data);
            }
            else {
              $('.row').last().after(data);  
            }
        },
        error:  function(xhr, str){
          //$('.row').last().after(data);
          alert('Exception ' + xhr.responseCode + ' str' + str + ' response' + xhr.responseText);
         }
      });
      return false;
    } 
  });
});