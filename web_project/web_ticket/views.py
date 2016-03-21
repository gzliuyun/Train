__author__ = 'a2'
from django.shortcuts import render
from web_ticket.forms import *
from web_ticket.models import *
import datetime

# Create your views here.

def login(request):
	errors = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user_name = cd['username']
			pass_word = cd['password']
			try:
				user = Users.objects.get(username=user_name)
			except Users.DoesNotExist:
				errors.append('No current user!')
				return render(request, 'html/login.html', {'errors': errors, 'form': form})
			else:
				if not pass_word == user.password:
					errors.append('Wrong password!')
					return render(request, 'html/login.html', {'errors': errors, 'form': form})
				else:
					request.session['currentuser'] = user_name
	else:
		form = LoginForm()
	return render(request, 'html/login.html', {'form': form})

def logout(request):
	del request.session['currentuser']
	return render(request, 'html/logout.html')

def register(request):
	errors = []
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user_name = cd['username']
			pass_word = cd['password']
			sure_password = cd['surepassword']
			real_name = cd['realname']
			id_card = cd['idcard']
			phone_number = cd['phonenumber']
			e_mail = cd['email']
			try:
				user = Users.objects.get(username=user_name)
			except Users.DoesNotExist:
				if not pass_word == sure_password:
					errors.append('Confirm password failed!')
					return render(request, 'html/register.html', {'errors': errors, 'form': form})
				else:
					p = Users.objects.create(username=user_name, password=pass_word, userid=user_name+str(random.randint(100000, 999999)),
											realname=real_name, idcard=id_card, phonenumber=phone_number, email=e_mail)
					p.save()
			else:
				errors.append('Username has been registered!')
				return render(request, 'html/register.html', {'errors': errors, 'form': form})
	else:
		form = RegisterForm()
	return render(request, 'html/register.html', {'form': form})

def homepage(request):
	return render(request, 'html/homepage.html')

def buy_ticket(request):
	return render(request, 'html/buy_ticket.html')

def search_ticket(request):
	errors = []
	if request.method == 'POST':
		traintickets = []
		form = SearchticketForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_station = cd['startstation']
			destination_ = cd['destination']
			start_date = cd['startdate']
			try:
				tickets= Ticketinfo.objects.filter(startstation=start_station,destination=destination_)
			except Ticketinfo.DoesNotExist:
				errors.append('There is no tickets between current stations')
				return render(request, 'html/search_ticket.html', {'errors': errors, 'form': form})
			else:
				for ticket in tickets:
					ticketcount = TicketCounts.objects.get(trainnumber=ticket.trainnumber, startdate=start_date)
					trainticket = {'trainnumber': ticket.trainnumber, 'startdate':start_date,
									'startstation': start_station, 'destination': destination_,
									'starttime': ticket.starttime, 'arrivetime': ticket.arrivetime,
									'businessseat': ticketcount.businessseat+ticketcount.businessseatback,
									'principalseat': ticketcount.principalseat+ticketcount.principalseatback,
									'firstclsseat': ticketcount.firstclassseat+ticketcount.firstclassseatback,
									'secondclassseat': ticketcount.secondclassseat+ticketcount.secondclassseatback,
									'advancedsoftsleeper': ticketcount.advancedsoftsleeper+ticketcount.advancedsoftsleeperback,
									'softsleeper': ticketcount.softsleeper+ticketcount.softsleeperback,
									'hardsleeper': ticasketcounts.hardsleeper+ticketcount.hardsleeperback,
									'softseat': ticketcount.softseat+ticketcount.softseatback,
									'hardseat': ticketcount.hardseat+ticketcount.hardseatback,
									'noseat':ticketcount.noseat+ticketcount.noseatback,
									'others': ticketcount.others+ticketcount.othersback}
					traintickets.append(trainticket)
			return render(request, 'html/search_ticket.html', {'traintickets':traintickets})
	else:
		form = SearchticketForm()
	return render(request, 'html/search_ticket.html', {'form': form})

def search_seat(request):
	if request.method == 'POST':
		seats = []
		form = SearchseatForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			train_number = cd['trainnumber']
			start_date = cd['startdate']
			ticketcount = TicketCount.objects.get(trainnumber=train_number, startdate=start_date)
			ticketinfo = TicketInfo.objects.get(trainnumber=train_number)
			if ticketcount.businessseat+ticketcount.businessseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'businessseat',
						'seatcount': ticketcount.businessseat+ticketcount.businessseatback, 'seatprice': ticketinfo.businessseatprice}
				seats.append(seat)
			if ticketcount.principalseat+ticketcount.principalseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'principalseat',
						'seatcount': ticketcount.principalseat+ticketcount.principalseatback, 'seatprice': ticketinfo.principalseatprice}
				seats.append(seat)
			if ticketcount.firstclassseat+ticketcount.firstclassseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'firstclassseat',
						'seatcount': ticketcount.firstclassseat+ticketcount.firstclassseatback, 'seatprice': ticketinfo.firstclassseatprice}
				seats.append(seat)
			if ticketcount.secondclassseat+ticketcount.secondclassseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'secondclassseat',
						'seatcount': ticketcount.secondclassseat+ticketcount.secondclassseatback, 'seatprice': ticketinfo.secondclassseatprice}
				seats.append(seat)
			if ticketcount.advancedsoftsleeper+ticketcount.advancedsoftsleeperback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'advancedsoftsleeper',
						'seatcount': ticketcount.advancedsoftsleeper+ticketcount.advancedsoftsleeperback, 'seatprice': ticketinfo.advancedsoftsleeperprice}
				seats.append(seat)
			if ticketcount.softsleeper+ticketcount.softsleeperback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'softsleeper',
						'seatcount': ticketcount.softsleeper+ticketcount.softsleeperback, 'seatprice': ticketinfo.softsleeperprice}
				seats.append(seat)
			if ticketcount.hardsleeper+ticketcount.hardsleeperback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'hardsleeper',
						'seatcount': ticketcount.hardsleeper+ticketcount.hardsleeperback, 'seatprice': ticketinfo.hardsleeperprice}
				seats.append(seat)
			if ticketcount.softseat+ticketcount.softseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'softseat',
						'seatcount': ticketcount.softseat+ticketcount.softseatback, 'seatprice': ticketinfo.softseatprice}
				seats.append(seat)
			if ticketcount.hardseat+ticketcount.hardseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'hardseat',
						'seatcount': ticketcount.hardseat+ticketcount.hardseatback, 'seatprice': ticketinfo.hardseatprice}
				seats.append(seat)
			if ticketcount.noseat+ticketcount.noseatback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'noseat',
						'seatcount': ticketcount.noseat+ticketcount.noseatback, 'seatprice': ticketinfo.noseatprice}
				seats.append(seat)
			if ticketcount.others+ticketcount.othersback > 0:
				seat = {'trainnumber': train_number, 'startdate': start_date, 'seattype': 'others',
						'seatcount': ticketcount.others+ticketcount.othersback, 'seatprice': ticketinfo.othersprice}
				seats.append(seat)
			return render(request, 'html/search_seat.html', {'seats': seats})
	else:
		form = SearchseatForm()
	return render(request, 'html/search_seat.html', {'form': form})

def submit_ticket(request):
	errors = []
	if request.method == 'POST':
		currentuser = request.session.get('currentuser', None)
		user = Users.objects.get(username=currentuser)
		form = SubmitForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			train_number = cd['trainnumber']
			start_date = cd['startdate']
			seat_type = cd['seattype']
			ticketcount = Ticketcounts.objects.get(trainnumber=train_number, startdate=start_date)
			if seat_type == 'businessseat':
				if ticketcount.businessseat > 0:
					ticketcout.businessseat -= 1
					ticketcount.save()
					seat_number = ticketcount.businessseattotal-ticketcount.businessseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.businessseatback > 0:
						ticketcount.businessseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'principalseat':
				if ticketcount.principalseat > 0:
					ticketcout.principalseat -= 1
					ticketcount.save()
					seat_number = ticketcount.principalseattotal-ticketcount.principalseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.principalseatback > 0:
						ticasketcount.principalseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'firstclassseat':
				if ticketcount.firstclassseat > 0:
					ticketcout.firstclassseat -= 1
					ticketcount.save()
					seat_number = ticketcount.firstclassseattotal-ticketcount.firstclassseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.firstclassseatback > 0:
						ticketcount.firstclassseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'secondclassseat':
				if ticketcount.secondclassseat > 0:
					ticketcout.secondclassseat -= 1
					ticketcount.save()
					seat_number = ticketcount.secondclassseattotal-ticketcount.secondclassseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.secondclassseatback > 0:
						ticketcount.secondclassseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'advancedsoftsleeper':
				if ticketcount.advancedsoftsleeper > 0:
					ticketcout.advancedsoftsleeper -= 1
					ticketcount.save()
					seat_number = ticketcount.advancedsoftsleepertotal-ticketcount.advancedsoftsleeper
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.advancedsoftsleeperback > 0:
						ticketcount.advancedsoftsleeperback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'softsleeper':
				if ticketcount.softsleeper > 0:
					ticketcout.softsleeper -= 1
					ticketcount.save()
					seat_number = ticketcount.softsleepertotal-ticketcount.softsleeper
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.softsleeperback > 0:
						ticketcount.softsleeperback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'hardsleeper':
				if ticketcount.hardsleeper > 0:
					ticketcout.hardsleeper -= 1
					ticketcount.save()
					seat_number = ticketcount.hardsleepertotal-ticketcount.hardsleeper
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.hardsleeperback > 0:
						ticketcount.hardsleeperback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'softseat':
				if ticketcount.softseat > 0:
					ticketcout.softseat -= 1
					ticketcount.save()
					seat_number = ticketcount.softseattotal-ticketcount.softseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.softseatback > 0:
						ticketcount.softseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'hardseat':
				if ticketcount.hardseat > 0:
					ticketcout.hardseat -= 1
					ticketcount.save()
					seat_number = ticketcount.hardseattotal-ticketcount.hardseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.hardseatback > 0:
						ticketcount.hardseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'noseat':
				if ticketcount.noseat > 0:
					ticketcout.noseat -= 1
					ticketcount.save()
					seat_number = ticketcount.noseattotal-ticketcount.noseat
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.noseatback > 0:
						ticketcount.noseatback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
			if seat_type == 'others':
				if ticketcount.others > 0:
					ticketcout.others -= 1
					ticketcount.save()
					seat_number = ticketcount.otherstotal-ticketcount.others
					order_date = datetime.datetime.now().date()
					order_number = currentuser+str(datetime.datetime.now()).replace('000','').replace('-','').replace(' ','').replace(':','').replace('.','')
					p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
											startdate=start_date, seattype=seat_type, seatnumber=seat_number)
					p.save()
				else:
					if ticketcount.othersback > 0:
						ticketcount.othersback -= 1
						ticketbacks = Ticketbacks.objects.filter(trainnumber=train_number, startdate=start_date, seattype=seat_type)
						for ticketback in ticketbacks:
							seat_number = ticketback.seatnumber
							ticketback.delete()
							break
						p = Orders.objects.create(ordernumber=order_number, orderdate=order_date, userid=user.userid, trainnumber=train_number,
												startdate=start_date, seattype=seat_type, seatnumber=seat_number)
						p.save()
					else:
						errors.append('There is no enough tickets')
						return render(request, 'html/submit_ticket.html', {'errors': errors, 'form': form})
	else:
		form = SubmitForm()
	return render(request, 'html/submit_ticket.html', {'form': form})

def check_orders(request):
	errors = []
	currentorders = []
	currentuser = request.session.get('currentuser', None)
	try:
		orders = Orders.objects.filter(username=currentuser)
	except Orders.DoesNotExist:
		errros.append('You haven\'t bought any ticket')
		return render(request, 'html/check_orders.html', {'errors': errors, 'currentorders': currentorders})
	else:
		for order in orders:
			train_number = order.trainnumber
			start_date = order.startdate
			ticketinfo = Ticketinfo.objects.get(trainnumber=train_number, startdate=start_date)
			currentorder = {'ordernumber': order.ordernumber, 'orderdate': order.orderdate, 'username': currentuser,
							'trainnumber': train_number, 'startdate': start_date, 'starttime': ticketinfo.starttime,
							'arrivetime': ticketinfo.arrivetime, 'startstation': ticketinfo.startstation, 'destination': ticketinfo.destination,
							'seattype': order.seattype, 'seatnumber': order.seatnumber, 'valid': order.valid}
			currentorders.append(currentorder)
	return render(request, 'html/check_orders.html', {'currentorders': currentorders})

def ticket_back(request):
	currentuser = request.session.get('currentuser', None)
	if request.method == 'POST':
		form = TicketbackForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			train_number = cd['trainnumber']
			start_date = cd['startdate']
			seat_type = cd['seattype']
			seat_number = cd['seatnumber']
			order_number = cd['ordernumber']
			order = Orders.objects.get(ordernumber=order_number)
			order.valid = False
			order.save()
			p = Ticketbacks.objects.create(trainnumber=train_number, startdate=start_date, seattype=seat_type, seatnumber=seat_number)
			p.save()
			ticketcount = TicketCount.objects.get(trainnumber=train_number, startdate=start_date)
			if seat_type == 'businessseat':
				ticketcount.businessseatback += 1
			if seat_type == 'principalseat':
				ticketcount.principalseatback += 1
			if seat_type == 'firstclassseat':
				ticketcount.firstclassseatback += 1
			if seat_type == 'secondclassseat':
				ticketcount.secondclassseatback += 1
			if seat_type == 'advancedsoftsleeper':
				ticketcount.advancedsoftsleeperback += 1
			if seat_type == 'softsleeper':
				ticketcount.softsleeperback += 1
			if seat_type == 'hardsleeper':
				ticketcount.hardsleeperback += 1
			if seat_type == 'softseat':
				ticketcount.softseatback += 1
			if seat_type == 'hardseat':
				ticketcount.hardseatback += 1
			if seat_type == 'noseat':
				ticketcount.noseatback += 1
			if seat_type == 'others':
				ticketcount.othersback += 1
			ticketcount.save()
	else:
		form = TicketbackForm()
	return render(request, 'html/ticket_back.html', {'form': form})

def personal_info(request):
	errors = []
	currentuser = request.session.get('currentuser', None)
	pcurrentuser = Users.objects.get(username=currentuser)
	if request.method == 'POST':
		form = PersoninfoForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user_name = cd['username']
			phone_number = cd['phonenumber']
			e_mail = cd['email']
			if not user_name == currentuser:
				try:
					user = Users.objects.get(username=user_name)
				except Users.DoesNotExist:
					pcurrentuser.username = user_name
				else:
					errors.append('Username has been registered!')
					return render(request, 'html/personal_infor.html', {'errors': errors, 'form': form})
			pcurrentuser.phonenumber = phone_number
			pcurrentuser.email = e_mail
			pcurrentuser.save()
		return render(request, 'html/personal_infor.html', {'form': form})
	else:
		username = pcurrentuser.username
		realname = pcurrentuser.realname
		idcard = pcurrentuser.idcard
		phonenumber = pcurrentuser.phonenumber
		email = pcurrentuser.email
		return render(request, 'html/personal_infor.html', {'username': username, 'realname': realname,
															'idcard': idcard, 'phonenumber': phonenumber, 'email': email})

def password(request):
	errors = []
	currentuser = request.session.get('currentuser', None)
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
