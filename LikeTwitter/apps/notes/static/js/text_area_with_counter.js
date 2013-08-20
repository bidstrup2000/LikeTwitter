jQuery(document).ready(function(){
jQuery("#id_symbol_count").text('Symbols count(min. 10):    ' + jQuery("#id_body").val().length);
jQuery("#id_body").keyup(function(){
jQuery("#id_symbol_count").text('Symbols count(min. 10):    ' + jQuery("#id_body").val().length);});
});