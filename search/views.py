from django.http import HttpResponse

# Create your views here.

def index(Request):
	return HttpResponse('<h1> This is working just fine </h1>')
