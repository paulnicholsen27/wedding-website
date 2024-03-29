from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from models import Message
from forms import MessageForm

def base(request):
	warning_given = request.session.get('browser_warning', False)
	answer = request.user_agent.browser.family
	if 'IE' in request.user_agent.browser.family and not warning_given:
		explorer = True
		request.session['browser_warning'] = True
	else:
		explorer = False
	return render_to_response("base.html", {'explorer':explorer, 'answer':answer}, RequestContext(request))

def faq(request):
	return render_to_response("faq.html", {}, RequestContext(request))

def wedding_party(request):
	return render_to_response("weddingparty.html", {}, RequestContext(request))


def location(request):
	return render_to_response("location.html", {}, RequestContext(request))


def story(request):
	return render_to_response("story.html", {}, RequestContext(request))


def guestbook(request):
	messages = Message.objects.all().order_by('-date')
	if request.method == 'POST':
		name = request.POST.get('name', None)
		message = request.POST.get('message', None)
		spam = request.POST.get('spam_catcher', None)
		if spam or 'href' in message or 'http' in message or '<a' in message:
			return redirect('http://www.law.cornell.edu/wex/inbox/state_anti-spam_laws')
		form = MessageForm(request.POST)
		if form.is_valid():
			if not Message.objects.filter(name=name, message=message):
				#prevents duplicate entries
				message = form.save()
	return render_to_response("guestbook.html", {'messages':messages}, RequestContext(request))


def map(request):
	return render_to_response("map.html", {}, RequestContext(request))


def lodging(request):
	return render_to_response("lodging.html", {}, RequestContext(request))


def afterparty(request):
	return render_to_response("afterparty.html", {}, RequestContext(request))