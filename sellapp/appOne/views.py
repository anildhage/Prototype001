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

def iphones(request, id):
    products = Product.objects.get(id=id)
    context = {
    'products' : products
    }
    return render(request, 'appOne/product_detail.html', context)