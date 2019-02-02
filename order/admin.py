from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	fieldsets = [
	('Product',{'fields':['product'],}),
	('Quantity',{'fields':['quantity'],}),
	('Price',{'fields':['price'],}),
	]
	readonly_fields = ['product', 'quantity', 'price']
	can_delete = False #cause we dont want to delete an order from admin terminal
	max_num = 0 #cause we dont want to add more products to an order 
	template = 'admin/order/tabular.html' #used to change a little OrderItemAdmin class mostly same

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'billingName', 'emailAddress', 'created']
	list_display_links = ('id', 'billingName')
	serach_fields = ['id', 'billingName', 'emailAddress']
	readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity', 'billingState', 'billingPostcode', 
						'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity', 'shippingState','shippingPostcode', 'shippingCountry']

	fieldsets = [
	('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
	('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress1', 'billingCity', 'billingState', 'billingPostcode', 'billingCountry', 'emailAddress']}),
	('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1', 'shippingCity', 'shippingState', 'shippingPostcode', 'shippingCountry']}),
	]

	inlines = [
		OrderItemAdmin,
	] #as in order to see the order items of the order record we are adding OrderItemAdmin as part of the OrderAdmin class

	search_fields = ['id', 'billingName']

	def has_delete_permission(self, request, obj = None):
		return False

	def has_add_permission(self, request):
		return False
