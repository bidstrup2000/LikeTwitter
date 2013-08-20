<script language="javascript" type="text/javascript">    
function call() {
    var msg   = $('#add_note').serialize();
    $.ajax({
        type: 'POST',
        url: 'add/',
        data: msg,
        success: function(data) {
            $('.row').after(data);
        },
        error:  function(xhr, str){
            alert('Возникла ошибка: ' + xhr.responseCode);
        }
    });
}
</script>