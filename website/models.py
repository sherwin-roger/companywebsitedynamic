from django.db import models
from django.contrib import admin
# Create your models here.

class company(models.Model):
    peoplename = models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    itemprice=models.IntegerField()

class companyAdmin(admin.ModelAdmin):
    list_display = ('peoplename', 'itemname', 'itemprice')