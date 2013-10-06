$(function(){

    $("ul.dropdown li").hover(function(){
    
        $(this).addClass("hover");
        $('ul:first',this).css('visibility', 'visible');
    
    }, function(){
    
        $(this).removeClass("hover");
        $('ul:first',this).css('visibility', 'hidden');
    
    });
    
    $("ul.dropdown li ul li:has(ul)").find("a:first").append(" &raquo; ");

});


$("#guest_submit").fancybox({
	'scrolling'	: true,
	helpers : {
		title : null
	}

});

$(document).ready(function(){
	$("#message_form").on("submit", function(){

		if ($("#guest_name").val().length < 1 || $("#guest_message").val().length < 1) {
		    $("#guest_error").show();
		    $.fancybox.resize();
		    return false;
		}

		$.fancybox.showActivity();
		$.ajax({
			type: "POST",
			cache: false,
			url: "/guestbook/",
			data: $(this).serializeArray(),
			success: function(data){
				$.fancybox(data);
			} 


		});
		return false;

	});
})

$(document).ready(function(){
	time_units = ["days", "hours", "minutes", "seconds", "milliseconds"];
	$("#clock").on("click", function(){
	})


var current_date;
var target_date = new Date("September 27, 2014 16:30:00").getTime();
var days, hours, minutes, seconds, milliseconds;
var countdown = document.getElementById("countdown");
if(countdown){
setInterval(function(){
	current_date = new Date().getTime();
	var milliseconds = target_date - current_date;
	var days = Math.floor(milliseconds / 1000 / 60 / 60 / 24);
	milliseconds -= (days * 1000 * 60 * 60 *24);
	hours = Math.floor(milliseconds / 1000 / 60 / 60);
	milliseconds -= (hours * 1000 * 60 * 60);
	minutes = Math.floor(milliseconds / 1000 / 60);
	milliseconds -= (minutes * 1000 * 60);
	seconds = Math.floor(milliseconds / 1000);
	milliseconds -= (seconds * 1000)

	countdown.innerHTML = days + " days, " + hours + " hours, " + minutes + " minutes, " + seconds + " seconds, " + milliseconds + " milliseconds";

}, 1);
}
})
// $("#newuser_fancy").fancybox({
// 	'scrolling'	: 'no',
// 	helpers : {
// 		title : null
// 	}
// });

// $("#newuser_form").bind("submit", function(){

// 	$.fancybox.showActivity();

// 	$.ajax({
// 		type: "POST",
// 		cache: false,
// 		url: "/data/new_user.html",
// 		data: $(this).serializeArray(),
// 		success: function(data){
// 			$.fancybox(data);
// 		} 


// 	});
// 	return false;

// });