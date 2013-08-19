jQuery(document).ready(function(){
    jQuery("#id_body").after("<p style="text-align:center;"><h1>Symbol count: </h1><input type="text"  id="id_symbol_count" value="0" maxlength="3" size="3" readonly=""> </p>");
    jQuery("#id_symbol_count").val(jQuery("#id_body").val().length);
    jQuery("#id_body").keyup( function() {
        jQuery("#id_symbol_count").val(jQuery("#id_body").val().length);
    });
});