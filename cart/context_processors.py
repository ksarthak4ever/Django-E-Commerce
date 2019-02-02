''' 
A context processor has a very simple interface: It’s a Python function that takes one argument, an HttpRequest object, and returns a dictionary that gets added to the template context. Each context processor must return a dictionary.

Custom context processors can live anywhere in your code base. All Django cares about is that your custom context processors are pointed to by the 'context_processors' option in your TEMPLATES setting — or the context_processors argument of Engine if you’re using it directly.
'''

#Used to give functionality to cart icon

from .models import Cart,CartItem
from .views import _cart_id

def counter(request): #Used to display no. of items in cart from navbar
	item_count = 0
	if 'admin' in request.path:
		return{}
	else:
		try:
			cart = Cart.objects.filter(cart_id=_cart_id(request))
			cart_items = CartItem.objects.all().filter(cart=cart[:1])
			for cart_item in cart_items:
				item_count += cart_item.quantity
		except Cart.DoesNotExist:
			item_count = 0
	return dict(item_count = item_count)