# Django-E-Commerce
This is an E-Commerce web application made using Django through which you can create an account,buy products of different categories,place an order using Stripe and recieve emails using Mailgun.

## How to setup and run the Project

* Set up a virtual environment and install django and the libraries used in this project from the requirements.txt file using:~
`pip install -r requirements.txt`

* Remember to run:~ `python manage.py collectstatic` 
command to collect static files into STATIC_ROOT

* To run the application enter command :~ `python manage.py runserver`

* To access stripe and mailgun features create your own account in their sites and add the api keys and password in settings.py file of perfectcushion directory accordingly.

* To create a fresh database remove the database file and the migrations and run commands:~
`python manage.py makemigrations`
`python manage.py migrate`

* For any queries contact me.

## Some Blogs i wrote while creating this project

* [How to interact with django shell using django ORM](https://medium.com/@ksarthak4ever/django-models-and-shell-8c48963d83a3)

* [How to use MongoDb with Django](https://medium.com/@ksarthak4ever/how-to-use-django-with-mongodb-40ba36a21124)
