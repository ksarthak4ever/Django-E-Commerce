''' 
A context processor has a very simple interface: It’s a Python function that takes one argument, an HttpRequest object, and returns a dictionary that gets added to the template context. Each context processor must return a dictionary.

Custom context processors can live anywhere in your code base. All Django cares about is that your custom context processors are pointed to by the 'context_processors' option in your TEMPLATES setting — or the context_processors argument of Engine if you’re using it directly.
'''

#using in order to make category links available accross the website

from .models import Category

def menu_links(request):
	links = Category.objects.all()
	return dict(links=links)