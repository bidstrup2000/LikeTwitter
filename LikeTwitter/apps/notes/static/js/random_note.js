$(document).ready(function(){
  $.ajax({
    url: 'random/',
    dataType: 'html',
    success: function(data) {
      $("#random_note").append(data)
    },
    error:  function(xhr, str){
    }
  });
})