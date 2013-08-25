from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response

def landing(request):
	return render_to_response("landing.html", {}, RequestContext(request))