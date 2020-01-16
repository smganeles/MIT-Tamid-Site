$(document).ready(function() {
	
	if (document.getElementById("animate").innerHTML == "True") {

		$("#CtoC").click(function() {

			$(".bottom").animate({
				top: "+=500px"
			}, 1000);

			var width = $(document).width();
			var height
			if (width > 1106) {
				height="99px"
			} else {
				height="145px"
			}

			$("#nav_box")
				.animate({height: height}, 1000)
				.queue(function (next) {
					$(this).css("height","auto");
					$("#head_overlay").css("box-shadow","0 0 15px 5px rgba(0,0,0,.2)");
					next();
				});

			$(".title").animate({
				fontSize:"115px"
			},1000);

			$("#nav_list").css("display", "flex");
			$("#nav_list").animate({
				opacity:"1"
			},1000);

			$("#TAMID").animate({
				marginTop: "20px"
			},1000);

			$("#AT_end").fadeIn(1000);
			$("#MIT_end").fadeIn(1000);

			$("#AT_MIT").delay(1000).hide(0);

			$(".container").css("height", "auto");

			$("#head_overlay").animate({
				'background-color': "rgba(67,121,176,0.5)"
			},1000);
		});

	} else {
		$("#TAMID").css("marginTop", "20px");
		$("#nav_box").css("height", "auto");
		$("#head_overlay").css("box-shadow","0 0 15px 5px rgba(0,0,0,.2)");

		$(".title").css("fontSize","115px");

		$("#nav_list").css({"display": "flex","opacity":"1"});

		$("#AT_end").show(0);
		$("#MIT_end").show(0);

		$("#AT_MIT").hide();

		$(".container").css("height", "auto");

		$("#head_overlay").css("background-color", "rgba(67,121,176,0.5)");
	}

	if ($("#username").html() == "") {
		console.log("no_user");
		$("#Welcome_msg").hide(0);
	} else {
		console.log("logged_in");
		$("#home_portal").hide(0);
	}


});




