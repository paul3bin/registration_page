from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'registration/index.html')

def registration(request):
    return render(request,'registration/registration.html')