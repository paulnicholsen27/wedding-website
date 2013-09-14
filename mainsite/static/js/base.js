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





$("#login_fancy").fancybox({
	'scrolling'	: true,
	helpers : {
		title : null
	}

});

$("#login_form").bind("submit", function(){
	console.log("login submitted");
	$.fancybox.showActivity();

	$.ajax({
		type: "POST",
		cache: false,
		url: "/login/",
		data: $(this).serializeArray(),
		success: function(data){
			$.fancybox(data);
		} 


	});
	return false;

});






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