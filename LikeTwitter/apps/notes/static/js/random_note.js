$(document).ready(function(){
  var random_note_url = ($("#random_note").attr('url') + ('random/'));
  $.ajax({
    crossDomain: true,
    url: random_note_url,
    dataType: 'jsonp',
    success: function(json) {
      $("#random_note").append(json.random_note)
    },
    error:  function(xhr, str){
    }
  });
})