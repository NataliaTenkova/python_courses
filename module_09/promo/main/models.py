from django.db import models
from django.contrib.auth.models import User

class UserApp(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, blank=True)

class Company(models.Model):
	name = models.CharField(max_length=100, blank=True)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class House(models.Model):
	city = models.CharField(max_length=40, blank=True)
	street = models.CharField(max_length=100, blank=True)
	number = models.CharField(max_length=20, blank=True)
	qty_flat = models.IntegerField()
	qty_entr = models.IntegerField()

class Flat(models.Model):
	house = models.ForeignKey(House, models.SET_NULL, blank=True, null=True)
	number = models.IntegerField()

class Reaction(models.Model):
	name = models.CharField(max_length=50, blank=True)

class User_Company(models.Model):
	user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
	company = models.ForeignKey(Company, models.SET_NULL, blank=True, null=True)

class House_Company(models.Model):
	house = models.ForeignKey(House, models.SET_NULL, blank=True, null=True)
	company = models.ForeignKey(Company, models.SET_NULL, blank=True, null=True)

class Flat_Company(models.Model):
	flat = models.ForeignKey(Flat, models.SET_NULL, blank=True, null=True)
	company = models.ForeignKey(Company, models.SET_NULL, blank=True, null=True)
	open_door = models.BooleanField()
	visit_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	contact = models.TextField()
	comment = models.TextField()
	react = models.ForeignKey(Reaction, models.SET_NULL, blank=True, null=True)



