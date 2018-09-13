from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader 
from .models import payslip

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
		r = preprocess(uploaded_file_url)
		for x in r:
			p = payslip(ECR_no = x[0],Pan = x[1],empl_no = x[2],Name = x[3],Father = x[4],Desgn = x[5],Dept =  x[6],acc_no =  x[7],PF_ac =  x[8],mo_inc = x[9],relief = x[10],basic_pay = x[11],d_pay = x[12],s_pay = x[13],s_all = x[14],p_pay = x[15],da    = x[16],i_relief = x[17],nra = x[18],ma = x[19],ca = x[20],wa = x[21],ha = x[22],misc = x[23],total_pay = x[24],pf = x[25],apf = x[26],pf_loan = x[27],lic = x[28],w_loan = x[29],i_tax = x[30],ebf = x[31],con_adv = x[32],hrc = x[33],fc = x[34],lc = x[35],wc = x[36],gss = x[37],sbi_ln = x[38],hb_loan = x[39],rop = x[40],uf = x[41],elec_ch = x[42],soc_ln = x[43],m_loan = x[44],f_adv = x[45],gar_ch = x[46],comp_ad = x[47],car_chr = x[48],misc2 = x[49],total_ded = x[50],net_pay = x[51],month =  x[52],year = x[53])
			p.save()
	return HttpResponse('<h1>This is working</h1>')
