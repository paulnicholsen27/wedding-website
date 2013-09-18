from django.template import loader, RequestContext
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def base(request):
	if request.method == "GET":
		return render_to_response("base.html", {}, RequestContext(request))
	else:
		response_dict = {'error' : None}
		if "login" in request.POST:
			email = request.POST.get('email', False)
			password = request.POST.get('password', False)
			if email and password:
				user = authenticate(username=email, password=password)
				response_dict.update({'email':email, 'password':password})
				if user:
					name = "{0} {1}.".format(user.first_name, user.last_name[0])
					print name
				else:
					response_dict['error'] = "No user found with that email/password."
			else:
				response_dict['error'] = "Please fill out all fields."
			if response_dict['error']:
				render_to_response("base.html", {'error_message':response_dict['error']}, RequestContext(request))
		elif "newuser" in request.POST:
			email = request.POST.get('email', False)
			password = request.POST.get('password', False)
			confirm = request.POST.get('confirm', False)
			first_name = request.POST.get('firstname', False)
			last_name = request.POST.get('lastname', False)
			if not all([email, password, confirm, first_name, last_name]):
				response_dict['error'] = "Please fill out all fields"
			elif password != confirm:
				response_dict['error'] = "Your passwords do not match.  They should."
			elif User.objects.filter(username=email).count():
				response_dict['error'] = "There is already a user with that email address."
			else:
				user = User.objects.create_user(
					username=email, 
					email=email, 
					password=password, 
					first_name=first_name, 
					last_name=last_name
				)
				user.save()
				user = authenticate(username=email, password=password)
				login(request,user)
		return render_to_response("base.html", {}, RequestContext(request))

def wedding_party(request):
	return render_to_response("weddingparty.html", {}, RequestContext(request))

def location(request):
	return render_to_response("location.html", {}, RequestContext(request))

def story(request):
	return render_to_response("story.html", {}, RequestContext(request))
# def login(request):
# 	response_dict = {}
# 	email = request.POST.get('email', False)
# 	password = request.POST.get('password', False)
# 	response_dict.update({'email': email, 'password':password})
# 	if not email or not password:
# 		response_dict['errors'] = "Please fill out all fields."
# 	return render_to_response("login.html", {}, RequestContext(request))

# def newuser(request):
# 	return render_to_response("newuser.html", {}, RequestContext(request))