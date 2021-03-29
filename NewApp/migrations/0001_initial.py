# Generated by Django 3.1.6 on 2021-02-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BILLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoiceno', models.CharField(max_length=200, null=True)),
                ('Vendorname', models.CharField(max_length=200, null=True)),
                ('Invoiceamount', models.FloatField(null=True)),
                ('grnamount', models.IntegerField(null=True)),
                ('paymentmode', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
