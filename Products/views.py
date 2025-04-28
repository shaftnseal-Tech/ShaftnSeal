from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

 # cache this view for 15 minutes (900 seconds)


# Create your views here.


def home(request):
    return render(request, 'Products/home.html')
   
cache_page(60*15)
def about(request):
    return render(request, 'Products/about.html')


cache_page(60*15)
def services(request):
    return render(request, 'Products/services.html')

cache_page(60*15)
def contact(request):
    return render(request, 'Products/contact.html')

cache_page(60*15)
def products(request):
    return render(request, 'Products/products.html')


def index(request):
    return redirect('home')  # redirects to the home URL pattern
