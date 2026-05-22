from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def catalog(request):
    return render(request,'main/catalog.html')

def product(request):
    return render(request,'main/product.html')

def avtorizeytion(request):
    return render(request,'main/avtorizeytion.html')

def registration(request):
    return render(request,'main/registration.html')

def profile(request):
    return render(request,'main/profile.html')