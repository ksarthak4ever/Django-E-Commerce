"""perfectcushion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings #importing settings 
from django.conf.urls.static import static #importing static after settings so we can map the static and media urls


urlpatterns = [

    path('admin/', admin.site.urls),

    path('cart/',include('cart.urls')),

    path('order/', include('order.urls')),

    path('account/create/', views.signupView, name = 'signup'),

    path('account/login/', views.signinView, name = 'signin'),

    path('account/logout/', views.signoutView, name = 'signout'),

    path('search/',include('search_app.urls')), 

    path('', include('shop.urls')), #The issue is caused by the shop app (Please keep in mind this setup is different) as Django is getting confused by the other apps and did not know whether or not it could resolve the cart, order and search apps' urls

]


if settings.DEBUG: #mapping static and media url when debug is enabled 
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)