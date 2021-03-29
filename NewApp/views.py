from django.shortcuts import render,redirect
from NewApp.models import BILLS
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def dashbord(request):
	return render(request,'Dashboard.html')
def input(request):
	return render(request, 'inputbills.html')
@csrf_exempt
def inputdata(request):
	date=request.POST.get('date')
	invnum=request.POST.get('invoiceno')
	vname=request.POST.get('vendorname')
	invamt=request.POST.get('invoiceamount')
	grnamt=request.POST.get('grnamount')
	pymode=request.POST.get('paymentmode')
	dbobj=BILLS(Invoiceno=invnum,Vendorname=vname,Invoiceamount=invamt,grnamount=grnamt,paymentmode=pymode,date=date)
	dbobj.save()
	
	obj=BILLS.objects.all()
	return render(request, 'Dashboard.html',{'msg':obj})
