from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def index(response):
	# пока пример из теории, заполню нужными данными
	data = {'data': [1, 2, 3], 'title': 'Index'}
	return render(response, "main/index.html", data)

def reg(response):
	return render(response, "main/reg.html")

def user(response):
	return render(response, "main/user.html")
