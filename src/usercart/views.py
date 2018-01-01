# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from carton.cart import Cart
from products.models import Product

# Create your views here.
def show(request):
	return render(request, 'usercart/usercart.html')

def add(request):
	cart = Cart(request.session)
	product = Product.objects.get(id=request.GET.get('id'))
	cart.add(product, price=product.price)
	return HttpResponse("Added to Cart. Return to Previous Page")

def remove(request):
	cart = Cart(request.session)
	product = Product.objects.get(id=request.GET.get('id'))
	cart.remove(product)
	return HttpResponse("Removed. Return to Previous Page & Refresh")

def menu(request):
	menu = Product.objects.all()
	return render(request, 'usercart/usercart.html', {'menu': menu})