from django.shortcuts import render
from goods.models import  Categories
def index(request):

    context = {

    }
    return render(request,'main/index.html',context)

def about(request):
    return render(request,'main/about.html')

def catalog(request):
    return render(request,'main/catalog.html')

def product(request):
    return render(request,'main/product.html')
