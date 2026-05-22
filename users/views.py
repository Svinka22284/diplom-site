from django.shortcuts import render

# Create your views here.
def avtorizeytion(request):
    context ={
        'title':'Home - Авторизація ',
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