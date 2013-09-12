$(document).ready(function(){
    $('form').submit(function()  {
        var msg   = $('#add_note').serialize();
        $.ajax({
            type: 'POST',
            url: 'notes/',
            data: msg,
            success: function(data) {
                $('.col-lg-8').last().after(data);
            },
            error:  function(xhr, str){
                alert('Exception ' + xhr.responseCode);
            }
        });
    return false;
    });
});