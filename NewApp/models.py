from django.db import models
# Create your models here.
class BILLS(models.Model):
	Invoiceno=models.CharField(max_length=200,null=True)
	Vendorname=models.CharField(max_length=200,null=True)
	Invoiceamount=models.FloatField(null=True)
	grnamount=models.IntegerField(null=True)
	paymentmode=models.CharField(max_length=200,null=True)
	date=models.DateTimeField(auto_now_add=True,null=True)
