from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'appOne/home.html', context)

def mobile(request):
    return render(request, 'appOne/mobile.html')

def mobile_detail(request, id):
    mobile = Product.objects.get(id=id)
    context = {
        'mobile' : mobile
    }
    return render(request, 'appOne/mobile_detail.html', context)

def pc(request):
    return render(request, 'appOne/pc.html')

def tablet(request):
    return render(request, 'appOne/tablet.html')   

def accessory(request):
    return render(request, 'appOne/accessories.html') 

def feedback(request):
    return render(request, 'appOne/feedback.html')

def adform(request):
    return render(request, 'appOne/adform.html')