from django.shortcuts import render
from datetime import datetime
#from django.http import HttpResponse

# Create your views here.
def register_user(request):
    year = datetime.now().year
    return render(request, 'signup.html', {'year': year})

def login_user(request):
    year = datetime.now().year
    return render(request, 'login.html', {'year': year})

def inicio(request):
    year = datetime.now().year
    return render(request, 'inicio.html', {'year': year})

def foro(request):
    year = datetime.now().year
    return render(request, 'foro.html', {'year': year})
