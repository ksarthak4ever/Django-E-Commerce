from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
	path('',views.allProdCat, name='allProdCat'),
	path('<slug:c_slug>/', views.allProdCat, name='products_by_category'), #view to show all products in a specific category
	path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'), #view for product details
]
