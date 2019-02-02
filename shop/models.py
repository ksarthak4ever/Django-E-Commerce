from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=250,unique=True)
	slug = models.SlugField(max_length=250,unique=True) #this will have the url path that the reciever requests on the browser
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category',blank=True) #blank=True tells that the field is not required to be filled in the forms online null=True which sets NULL on the column of our db

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):  #url tag will do the reverse operation and generate a url path, where as get_absolute_url should be defined in a model as this is to get url for a particular object.
		return reverse('shop:products_by_category', args=[self.slug]) #Given a url pattern, Django uses url() to pick the right view and generate a page. That is, url--> view name. But sometimes, like when redirecting, you need to go in the reverse direction and give Django the name of a view, and Django generates the appropriate url. In other words, view name --> url. That is, reverse() (it's the reverse of the url function).

	def __str__(self): #dunder(i.e double underscore) str method is used to make posts readable in the python shell where we acess the database
		return '{}'.format(self.name)


class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True) #this will have the url path that the reciever requests on the browser
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) #If the product is deleted then any reference of that product at the category model will be also deleted
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True) #default=True because we want this option to be ticked on by default
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)


