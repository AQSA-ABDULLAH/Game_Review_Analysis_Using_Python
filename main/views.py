from django.shortcuts import render;
from .models import Game;
from .form import SignupForm

def home(request):
	data = Game.objects.all().order_by('-id')
	return render(request,'index.html', {'data':data})

def login(request):
	return render(request,'login.html')

def signup(request):
	form=SignupForm
	return render(request,'signup.html', {'form':form})