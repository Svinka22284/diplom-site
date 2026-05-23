from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


# Create your views here.
def avtorizeytion(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else: form = UserLoginForm()
    context ={
        'title':'Home - Авторизація ',
        'form':form,
    }
    return render(request,'users/avtorizeytion.html',context)

def registration(request):
    context = {
        'title': 'Home - Реєстрація ',
    }
    return render(request,'users/registration.html',context)

def profile(request):
    context = {
        'title': 'Home - Кабінет ',
    }
    return render(request,'users/profile.html',context)

def logout(request):
    ...
    return render(request,'users/logout.html')