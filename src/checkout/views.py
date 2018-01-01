# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
from carton.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY 

# Create your views here.

@login_required
def checkout(request):
	finalcart = Cart(request.session)
	total = finalcart.total
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		customer = stripe.Customer.retrieve(customer_id)
		customer.sources.create(source=token)
		# Charge the user's card:
		charge = stripe.Charge.create(
  			amount=int(total*100)/2,
  			currency="usd",
  			description="Example charge",
  			customer=customer,
		 )
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request,template,context)
