from django.http import HttpResponse

def log_in(request):
	#Here should contain the login page template later.
    return HttpResponse("log_in")

def register(request):
	#Here should contain the register page template later.
	return HttpResponse("register")
	
def main_page(request):
	#Here should contain the main page template later.
	return HttpResponse("main_page")

def buy_ticket(request):
	#Here should contain the ticket perchase page template later.
	return HttpResponse("buy_ticket")
	
def check_ticket(request):
	#Here should contain the page template for checking the ticket already bought later.
	return HttpResponse("check_ticket")
	
def query_ticket(request):
	#Here should contain the ticket query page template later.
	return HttpResponse("query_ticket")
	
def personal_info(request):
	#Here should contain the page template to check user information later.
	return HttpResponse("personal_info")