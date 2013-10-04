jQuery(document).ready(function(){
	jQuery("input[type=Submit]").attr("disabled","disabled")
	jQuery("#id_symbol_count").text('Symbols count(min. 10):    ' + jQuery("#id_body").val().length);
	jQuery("#id_body").keyup(function(){
		jQuery("#id_symbol_count").text('Symbols count(min. 10):    ' + jQuery("#id_body").val().length);
		if (jQuery("#id_body").val().length > 9) {
			jQuery("input[type=Submit]").removeAttr("disabled");
		}
		else {
			jQuery("input[type=Submit]").attr("disabled","disabled")
		}
	});
});
