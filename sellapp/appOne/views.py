from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
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

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']# add enctype="multipart/form-data" in the form
        product = Product(name = name, price = price, desc = desc, image = image)
        product.save()
    return render(request, 'appOne/add_product.html')


def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']# add enctype="multipart/form-data" in the form
        product.save()
        return redirect('/')
    context = {
        'product' : product
    }
    return render(request, 'appOne/update_product.html', context)

def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {
        'product' : product
    }
    return render(request, 'appOne/delete_product.html', context)