from django.shortcuts import render
import os
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth import logout as django_logout
 
from django.utils import translation
from .models import *
# Create your views here.
#def irm_login(request):
 #   return render(request, "home.html")

#def signup(request):
 #   return render(request, "signup.html")

def index(request): 
	if request.method == 'POST':
		print("post")
		email = request.POST.get('email')
		password = request.POST.get('password')
		user  = authenticate(email = email , password = password)
		if user is not None :
			login(request, user)
			print("logged in"+ user.username)
			username = user.username
			context = {'username' : username}
			return render(request,'irm_login_template/html/ecommerce/index.html', context)
		else:
			print("wrong usuername or pass")
			return JsonResponse({'success':False},status=400)
	context_dict = {"login_status":"False"}
	destpath = os.path.join("irm_login_template/html/pages/auths", "auth-login.html")

	return render(request,destpath ,context_dict)

def register(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = Irm_user.objects.create_user(username=username,
		email=email,
		password = password,
		)
		user.save()
		login(request,user)
		request.method = 'GET'
		return dashboard(request)
	else:
		return render(request, 'irm_login_template/html/pages/auths/auth-register.html')
		#irm_login_template/html/pages/auths/auth-register.html

def dashboard(request):
	if request.user.is_authenticated:
		context = {'username' : request.user.username}
		request.method = "GET"
		return render(request,'irm_login_template/html/ecommerce/index.html', context)
	else:
		return index(request)
def logout(request):
	context ={}
	django_logout(request)
	return render(request, 'irm_login_template/html/pages/auths/auth-login.html', context)



