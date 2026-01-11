from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def catalog(request):
    return render(request,'main/catalog.html')

def product(request):
    return render(request,'main/product.html')
