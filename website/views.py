from django.shortcuts import render
from .models import company
# Create your views here.

def home(request):
    context = {}
    return render(request, 'website/home.html', context)

def products(request):
    context = {}
    context["products"]=company.objects.all()
    return render(request, 'website/products.html', context)    

def people(request):
    context = {}
    context["companies"]=company.objects.all()
    return render(request, 'website/people.html', context)   

def contact(request):
    context = {}
    return render(request, 'website/contact.html', context) 