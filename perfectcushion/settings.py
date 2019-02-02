"""
Django settings for perfectcushion project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '80buif6-69k5yj2(4jx=*ug)$_n-2$$5n5t6-9ac$!f759#*wo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'search_app.apps.SearchAppConfig',
    'cart.apps.CartConfig',
    'stripe',
    'crispy_forms', 
    'order.apps.OrderConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'perfectcushion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'shop', 'templates/'), os.path.join(BASE_DIR, 'search_app', 'templates/'), os.path.join(BASE_DIR, 'cart', 'templates/'), os.path.join(BASE_DIR, 'order', 'templates/') ], #to make the apps templates available throughout the project
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.menu_links', #adding the location of our context_processor.py file
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'perfectcushion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

''' Since we have two image fields in our models declaration so we need to put some configurations in the settings file in order to make sure the images are uploaded to the right location '''

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #declaring static root which is where our static files will be stored
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')

#Stripe Settings for Payment

STRIPE_PUBLISHABLE_KEY = 'pk_test_FxqJcM5pDsQYvjqvomn1HTO3'
STRIPE_SECRET_KEY = 'sk_test_raf6Azr4OiG3htCp5SCYpYO6' #these are stripe api keys used for production for launch we would have to get the life key as mentioned in the stripe documentations you get them after making an account

CRISPY_TEMPLATE_PACK = 'bootstrap4' #using crispy form as it applies the right bootstrap classes to the forms 

#Email Settings using Mailgun

EMAIL_HOST = 'smtp.mailgun.org' #smpt is Simple Mail Transfer Protocol
EMAIL_PORT = '587' #this is a secured port that uses TLS(Transport Layer Security) Encryption
EMAIL_USE_TLS = True #as the port is using TLS
EMAIL_HOST_USER = 'postmaster@sandbox6ceb3bccd31549d48024fe4cc405c38d.mailgun.org' #using mailgun sandbox as it is free after we create an free acount
EMAIL_HOST_PASSWORD = 'b814dd8cc648e3f60f70149926c2b21e-c8c889c9-cbd24725' 