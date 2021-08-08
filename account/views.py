from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm



def dashboard_view(request):
    return render(request, "account/dashboard.html")

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			contact = form.cleaned_data.get('phone_number')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, phone_number=contact, email=email, password=raw_password)
			user = authenticate(email=email, password=raw_password)
			login(request, user)   
			return redirect("dashboard_view")		
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def login_view(request):
	context = {}
 
	if request.user.is_authenticated:
		return redirect("dashboard_view")
	else:
		if request.POST:
			form = AccountAuthenticationForm(request.POST)
			if form.is_valid():
				username = request.POST['email']
				password = request.POST['password']
				user = authenticate(email=username, password=password)

				if user:
					login(request, user)
					return redirect("dashboard_view")
		else:
			form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def account_view(request):    
	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"username" 		: request.POST['username'],
					"email" 		: request.POST['email'],
					"phone_number" 	:request.POST['phone_number'],
			}
			form.save()
			context['success_message'] = f"{request.user.username}'s profile updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
					"phone_number": request.user.phone_number,

				}
			)
	context['account_form'] = form
 
	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})


