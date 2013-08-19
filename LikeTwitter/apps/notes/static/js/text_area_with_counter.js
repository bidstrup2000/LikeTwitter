jQuery(document).ready(function(){
jQuery("#id_body").after('<label for="id_symbol_count"> Symbols count (min. 10):</label><input type="text"  id="id_symbol_count" value="0" maxlength="3" size="3" readonly="">');
jQuery("#id_symbol_count").val(jQuery("#id_body").val().length);
jQuery("#id_body").keyup( function() {
jQuery("#id_symbol_count").val(jQuery("#id_body").val().length);});
});