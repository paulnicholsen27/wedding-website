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


var current_date = new Date().getTime();
var target_date = new Date("September 27, 2014 16:30:00").getTime();
var days, hours, minutes, seconds, milliseconds;
var countdown = document.getElementById("countdown");

setInterval(function(){
	var milliseconds_left = target_date = current_date;
	countdown.innerHTML = milliseconds_left;
}, 1);
	console.log(milliseconds_left);
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