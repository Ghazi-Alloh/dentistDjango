from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def product(request):
    return render(request,'accounts/product.html')

def customer(request):
    return HttpResponse("customer page")
