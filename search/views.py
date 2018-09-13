from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader 
from .models import payslip, ExcelFile

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .preprocess import preprocess

def index(request):
	#template = loader.get_template('search/index.html')
	return render(request,'search/index.html')
	
	
	
def result(request):
	month = request.POST['month']
	year = request.POST['year']
	pan = request.POST['pan']
	empl_no = request.POST['empl_no']
	return HttpResponse("<h1>This is working :"+str(month)+str(year)+str(pan)+str(empl_no)+"</h1>")
	
def upload(request):
	return render(request,'search/upload.html')
	
def process(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		preprocess(uploaded_file_url)
	
	return HttpResponse('<h1>This is working</h1>')
