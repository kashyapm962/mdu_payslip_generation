from django.contrib import admin
from .models import payslip, ExcelFile
# Register your models here.
admin.site.register(payslip)
admin.site.register(ExcelFile)
