from django.shortcuts import render
from shop.models import Product
from django.db.models import Q #importing Q objects to provide search functionality to the site

''' Keyword argument queries – in filter(), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

A Q object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments. These keyword arguments are specified as in “Field lookups” above. '''

 
def searchResult(request):
	products = None
	query = None
	if 'q' in request.GET: #checking if there is a search request
		query = request.GET.get('q')
		products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query)) #searching products by queries
	return render(request,'search.html', {'query':query, 'products':products})
