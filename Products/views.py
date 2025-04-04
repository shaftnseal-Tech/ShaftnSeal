from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'Products/home.html')
   

def about(request):
    return render(request, 'Products/about.html')

def services(request):
    return render(request, 'Products/services.html')

def contact(request):
    return render(request, 'Products/contact.html')

def products(request):
    return render(request, 'Products/products.html')
from django.shortcuts import redirect

def index(request):
    return redirect('home')  # redirects to the home URL pattern
