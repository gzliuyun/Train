from django.db import models

class Ticket(models.Model):
    trainnumber = models.CharField(max_length=20)
    startstation = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    starttime = models.TimeField()
    arrivetime = models.TimeField()
    startdate = models.DateField()
    businessseat = models.IntegerField(blank=True)
    principalseat = models.IntegerField(blank=True)
    firstclassseat = models.IntegerField(blank=True)
    secondclassseat = models.IntegerField(blank=True)
    advancedsoftsleeper = models.IntegerField(blank=True)
    softsleeper = models.IntegerField(blank=True)
    hardsleeper = models.IntegerField(blank=True)
    softseat = models.IntegerField(blank=True)
    hardseat = models.IntegerField(blank=True)
    noseat = models.IntegerField(blank=True)
    others = models.IntegerField(blank=True)

	
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    cardid = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    orders = models.ManyToManyField(Ticket, blank=True)

