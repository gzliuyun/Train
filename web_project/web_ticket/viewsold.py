from django.shortcuts import render
from django.http import HttpResponse
from web_ticket.forms import *
from web_ticket.models import *

# Create your views here.

def login(request):
	errors = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = cd['username']
			passwd = cd['password']
			try:
				usr = Users.objects.get(username=user)
			except Users.DoesNotExist: 
				errors.append('No current user!')
				return render(request, 'html/login.html', {'errors': errors, 'form': form})
			else:
				if not passwd == usr.password:
					errors.append('Wrong password!')
					return render(request, 'html/login.html', {'errors': errors, 'form': form})
				else:
					request.session['currentuser'] = user
	else:
		form = LoginForm()
	return render(request, 'html/login.html', {'form': form})

def logout(request):
	del request.session['currentuser']
	return HttpResponse('you have logout!')

def register(request):
	errors = []
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = cd['username']
			passwd = cd['password']
			srpasswd = cd['surepassword']
			name = cd['realname']
			card = cd['idcard']
			phone = cd['phonenumber']
			mail = cd['email']
			try:
				usr = Users.objects.get(username=user)
			except Users.DoesNotExist:
				if not passwd == srpasswd:
					errors.append('Confirm password failed!')
					return render(request, 'html/register.html', {'errors': errors, 'form': form})
				else:
					p = Users.objects.create(username=user, password=passwd, userid=user+str(random.randint(100000, 999999)), realname=name, idcard=card, phonenumber=phone, email=mail)
					p.save()
			else:
				errors.append('Username has been registered!')
				return render(request, 'html/register.html', {'errors': errors, 'form': form})
	else:
		form = RegisterForm()
	return render(request, 'html/register.html', {'form': form})
	
def homepage(request):
	#Here should contain the main page template later.
	return HttpResponse("homepage")

def buy_ticket(request):
	#Here should contain the ticket perchase page template later.
	return HttpResponse("buy_ticket")
	
def find_ticket(request):
	#Here should contain the page template for checking the ticket already bought later.
	return HttpResponse("find_ticket")

def personal_info(request):
	errors = []
	currentuser = request.session.get('currentuser', None)
	pcurrentuser = Users.objects.get(username=currentuser)
	if request.method == 'POST':
		form = PersonInfoForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = cd['username']
			phone = cd['phonenumber']
			mail = cd['email']
			if not user == currentuser:
				try:
					usr = Users.objects.get(username=user)
				except Users.DoesNotExist:
					pcurrentuser.username = user
				else:
					errors.append('Username has been registered!')
					return render(request, 'html/personal_infor.html', {'errors': errors, 'form': form})
			pcurrentuser.phonenumber = phone
			pcurrentuser.email = mail
			pcurrentuser.save()
		return render(request, 'html/personal_infor.html', {'form': form})
	else:
		username = pcurrentuser.username
		realname = pcurrentuser.realname
		idcard = pcurrentuser.idcard
		phonenumber = pcurrentuser.phonenumber
		email = pcurrentuser.email
		return render(request, 'html/personal_infor.html', {'username': username, 'realname': realname, 'idcard': idcard, 'phonenumber': phonenumber, 'email': email})
	
def password(request):
	errors = []
	currentuser = request.session.get('username', None)
	pcurrentuser = Users.objects.get(username=currentuser)
	if request.method == 'POST':
		form = PasswordForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			oldpassword = cd['oldpassword']
			newpassword = cd['newpassword']
			surepassword = cd['surepassword']
			if not oldpassword == pcurrentuser.password:
				errors.append('Wrong password!')
				return render(request, 'html/password.html', {'errors': errors, 'form': form})
			else:
				if not newpassword == surepassword:
					errors.append('Confirm password failed!')
					return render(request, 'html/password.html', {'errors': errors, 'form': form})
				else:
					pcurrentuser = Users.objects.create(password=newpassword)
					pcurrentuser.save()
	else:
		form = PasswordForm()
	return render(request, 'html/password.html', {'form': form})
