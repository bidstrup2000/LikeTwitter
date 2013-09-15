$(document).ready(function(){
  $.ajax({
    type: 'GET',
    url: 'random/',
    success: function(data) {
      $('#random_note').text(data)
    }
    error:  function(xhr, str){
    //$('.row').last().after(data);
    alert('Exception ' + xhr.responseCode);
    }
  });
});