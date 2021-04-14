from django.shortcuts import render
from . import forms, models
# Create your views here.


def index(request):
    if request.method == 'POST':
        return registration(request)
    return render(request, 'registration/index.html')


def registration(request):
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
        else:
            print('Form invalid!')
    return render(request, 'registration/registration.html', context={'formkey': form})


def thanks(request):
    if request.method == 'POST':
        return index(request)
    return render(request, 'registration/thanks.html')
