from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem 
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import Order,OrderItem
from django.template.loader import get_template
from django.core.mail import EmailMessage


def _cart_id(request): #checking if a session id has been created on the customer browser
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

def add_cart(request, product_id):
	product = Product.objects.get(id = product_id)
	try: #getting a cart by id and if it does'nt exist then we will create the cart
		cart = Cart.objects.get(cart_id = _cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
				cart_id = _cart_id(request)
			)
		cart.save()
	try:
		cart_item = CartItem.objects.get(product = product, cart = cart) #adding product to cart
		if cart_item.quantity < cart_item.product.stock:
			cart_item.quantity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
				product = product,
				quantity = 1,
				cart = cart
			)
		cart_item.save()
	return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None): #this method is used to display cart
	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, active=True)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			counter += cart_item.quantity
	except ObjectDoesNotExist:
		pass

	stripe.api_key = settings.STRIPE_SECRET_KEY #processing payments using stripe api
	stripe_total = int(total * 100)
	description = 'Perfect Cushion Store - New Order'
	data_key = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST': #doing this to get the stripe token and email address in order to create the customer record and the charge
		try: 
			token = request.POST['stripeToken']
			email = request.POST['stripeEmail']
			billingName = request.POST['stripeBillingName'] #to get Billing Name from stripe payment form
			billingAddress1 = request.POST['stripeBillingAddressLine1']
			billingCity = request.POST['stripeBillingAddressCity']
			billingState = request.POST['stripeBillingAddressState']
			billingPostcode = request.POST['stripeBillingAddressZip']
			billingCountry = request.POST['stripeBillingAddressCountryCode']
			shippingName = request.POST['stripeShippingName']
			shippingAddress1 = request.POST['stripeShippingAddressLine1']
			shippingCity = request.POST['stripeShippingAddressCity']
			shippingState = request.POST['stripeShippingAddressState']
			shippingPostcode = request.POST['stripeShippingAddressZip']
			shippingCountry = request.POST['stripeShippingAddressCountryCode']
			customer = stripe.Customer.create(
						email=email,
						source=token
				)
			charge = stripe.Charge.create(
						amount=stripe_total,
						currency='gbp',
						description=description,
						customer=customer.id
				)
			''' Creating the Order '''
			try:
				order_details = Order.objects.create(
						token = token,
						total = total,
						emailAddress = email, 
						billingName = billingName,
						billingAddress1 = billingAddress1,
						billingCity = billingCity,
						billingState = billingState,
						billingPostcode = billingPostcode,
						billingCountry = billingCountry,
						shippingName = shippingName,
						shippingAddress1 = shippingAddress1,
						shippingCity = shippingCity,
						shippingState = shippingState,
						shippingPostcode = shippingPostcode,
						shippingCountry = shippingCountry
					)
				order_details.save()
				for order_item in cart_items: #every time the for loop runs a cart item is assigned to the order item variable
					oi = OrderItem.objects.create(
							product = order_item.product.name,
							quantity = order_item.quantity,
							price = order_item.product.price,
							order = order_details
						) #oi variable is getting the value of each order item in order to create the order item record
					oi.save()
					'''Reduce stock when order is placed or saved'''
					products = Product.objects.get(id = order_item.product.id)
					products.stock = int(order_item.product.stock - order_item.quantity)
					products.save()
					order_item.delete()
					'''The terminal will print this message when the order is saved'''
					print('The order has been created')
				try:
					''' Calling the sendEmail function '''
					sendEmail(order_details.id)
					print('The order email has been sent to the customer.')
				except IOError as e:
					return e
				return redirect('order:thanks', order_details.id)
			except ObjectDoesNotExist:
				pass
		except stripe.error.CardError as e:
			return False,e

	return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter, data_key = data_key, stripe_total = stripe_total, description = description))


def cart_remove(request, product_id): #to remove a quantity product from cart
	cart = Cart.objects.get(cart_id = _cart_id(request))
	product = get_object_or_404(Product, id = product_id)
	cart_item = CartItem.objects.get(product = product, cart = cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart:cart_detail')


def full_remove(request, product_id): #to remove the entire stock of a product from cart
	cart = Cart.objects.get(cart_id = _cart_id(request))
	product = get_object_or_404(Product, id = product_id)
	cart_item = CartItem.objects.get(product = product, cart = cart)
	cart_item.delete()
	return redirect('cart:cart_detail')

def sendEmail(order_id):
	transaction = Order.objects.get(id=order_id)
	order_items = OrderItem.objects.filter(order=transaction)
	try:
		'''Sending the order'''
		subject = "Perfect Cushion Store - New Order #{}".format(transaction.id) #using the transaction method to interpolate the transaction id in the curly brackets of the subject
		to = ['{}'.format(transaction.emailAddress)]
		from_email = "orders@perfectcushionstore.com"
		order_information = {
		'transaction' : transaction,
		'order_items' :	order_items
		}
		message = get_template('email/email.html').render(order_information)
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		msg.content_subtype = 'html'
		msg.send()
	except IOError as e:
		return e
