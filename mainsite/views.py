from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response

def base(request):
	return render_to_response("base.html", {}, RequestContext(request))
