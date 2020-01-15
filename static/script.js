$(document).ready(function() {

	$("#signup").click(function() {
		if ($(".confirm").css("display")=="none") {
			$(".confirm").fadeIn(1000);
		} else {
			var Correct = true;
			if ($("#cnfrm").val()==$("#pwd").val()) {
				$("#no_match").animate({
					opacity:0
				},400);
			} else {
				$("#no_match").animate({
					opacity:1
				},400);
				Correct=false;
			}
			if ($("#key").val()=="TAMID") {
				$("#no_key").animate({
					opacity:0
				},400);
			} else {
				$("#no_key").animate({
					opacity:1
				},400);
				Correct=false;
			}
			if (Correct == true) {
				$("#signup").removeAttr("type").attr("type","submit");
			}
		} //end else
	});


	$(".show").click(function() {
		$("#pwd").removeAttr("type").attr("type","text");
		$("#cnfrm").removeAttr("type").attr("type","text");
	});


	if ($("#logged_in").html()=="") {
		$("#portal").show(0);
		$("#drive_links").hide(0);
	} else {
		$("#portal").hide(0);
		$("#drive_links").show(0);
	}

});
