from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from models import Image


def photo_album(request):
	images = Image.objects.all()
	for image in images:
		print image.title
	return render_to_response("album.html", {'images':images}, RequestContext(request))