$(document).ready(function() {
	var panels = $.cookie(); //get all cookies
	for (var panel in panels){ //<-- panel is the name of the cookie
		if ($("#"+panel).hasClass('collapse')) {
			if($.cookie(panel) == 1){
				$("#" + panel).collapse('show');
            	// $("#" + panel).attr('class', 'collapse in');
            	$("#" + panel + 'Arrow').html('<i class="fa fa-fw fa-caret-up"></i>');
        	}
        }
    }

	$("ul").on("hide.bs.collapse", function(){
		var ulid = this.id;
		$.cookie(ulid, '0');
		ulid = '#' + ulid + 'Arrow';
		$(ulid).html('<i class="fa fa-fw fa-caret-down"></i>');
	});
	$("ul").on("show.bs.collapse", function(){
		var ulid = this.id;
		$.cookie(ulid, '1');
		ulid = '#' + ulid + 'Arrow';
		$(ulid).html('<i class="fa fa-fw fa-caret-up"></i>');
	});
});