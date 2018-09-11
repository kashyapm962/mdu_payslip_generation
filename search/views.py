from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django import forms  
# Create your views here.

def index(request):
	#template = loader.get_template('search/index.html')
	return render(request,'search/index.html')
	
	
	
def result(request):
	form = forms.ContactForm()
	return HttpResponse("<h1>This is working :"+ str(form)+"</h1>",year)
