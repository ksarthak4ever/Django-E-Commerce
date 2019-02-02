from django.contrib import admin
from .models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)} #used to assign the value of the name field to the slug field and the slug field is gonna be formatted into lowercase and also where there are gonna be a space in the name will be replaced by a Hyphen(-)
admin.site.register(Category,CategoryAdmin) #registering the model Category

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','price','stock','available','created','updated']
	list_editable = ['price','stock','available'] #this will give us flexibility to edit the product on the product interface(in admin) without accessing the product itself i.e no need to enter each product then edit one by one just edit all products at a same page outside in the product interface
	prepopulated_fields = {'slug':('name',)}
	list_per_page = 20
admin.site.register(Product,ProductAdmin)


