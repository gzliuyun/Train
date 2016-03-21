from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
	surepassword = forms.CharField(max_length=20)
	realname = forms.CharField(max_length=20)
	idcard = forms.CharField(max_length=20)
	phonenumber = forms.CharField(max_length=20)
	email = forms.EmailField(required=False)

class PersoninfoForm(forms.Form):
	username = forms.CharField(max_length=20)
	realname = forms.CharField(max_length=20)
	idcard = forms.CharField(max_length=20)
	phonenumber = forms.CharField(max_length=20)
	email = forms.EmailField(required=False)

class PasswordForm(forms.Form):
	oldpassword = forms.CharField(max_length=20)
	newpassword = forms.CharField(max_length=20)
	surepassword = forms.CharField(max_length=20)

class SearchticketForm(forms.Form):
	startstation = forms.CharField(max_length=20)
	destination = forms.CharField(max_length=20)
	startdate = forms.DateField()

class SearchseatForm(forms.Form):
	trainnumber = forms.CharField(max_length=20)
	startdate = forms.DateField()
	startstation = forms.CharField(max_length=20)
	destination = forms.CharField(max_length=20)
	starttime = forms.TimeField()
	arrivetime = forms.TimeField()
	businessseat = forms.IntegerField()
	principalseat = forms.IntegerField()
	firstclassseat = forms.IntegerField()
	secondclassseat = forms.IntegerField()
	advancedsoftsleeper = forms.IntegerField()
	softsleeper = forms.IntegerField()
	hardsleeper = forms.IntegerField()
	softseat = forms.IntegerField()
	hardseat = forms.IntegerField()
	noseat = forms.IntegerField()
	others = forms.IntegerField()

class SubmitForm(forms.Form):
	trainnumber = forms.CharField(max_length=20)
	startdate = forms.DateField()
	seattype = forms.CharField(max_length=20)
	seatcount = forms.IntegerField()
	seatprice = forms.IntegerField()

class TicketbackForm(forms.Form):
	ordernumber = forms.CharField(max_length=50)
	orderdate = forms.DateField()
	username = forms.CharField(max_length=20)
	trainnumber = forms.CharField(max_length=20)
	startdate = forms.DateField()
	starttime = forms.TimeField()
	arrivetime = forms.TimeField()
	startstation = forms.CharField(max_length=20)
	destination = forms.CharField(max_length=20)
	seattype = forms.CharField(max_length=20)
	seatnumber = forms.IntegerField()
	valid = forms.BooleanField()
