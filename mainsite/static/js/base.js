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
		else{
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
	}
	});
})





$("#newuser_fancy").fancybox({
	'scrolling'	: 'no',
	helpers : {
		title : null
	}
});

$("#newuser_form").bind("submit", function(){

	$.fancybox.showActivity();

	$.ajax({
		type: "POST",
		cache: false,
		url: "/data/new_user.html",
		data: $(this).serializeArray(),
		success: function(data){
			$.fancybox(data);
		} 


	});
	return false;

});