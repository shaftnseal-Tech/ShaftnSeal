from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.http import HttpResponse,Http404

# cache this view for 15 minutes (900 seconds)

# Create your views here.
def home(request):
    search_data = request.GET.get('q','').lower()
    
    if search_data:
        try:
            if 'spares' in search_data:
                return redirect('spares_page')
            elif 'product' in search_data:
                return redirect('products')
            elif 'energy' in search_data or 'efficiency' in search_data:
                return redirect('Energy_efficiency_home')
            elif 'services' in search_data or 'service' in search_data:
                return redirect('service_page')
            elif 'pump' in search_data or 'service' in search_data:
                return redirect('pump')
            else:
                return redirect('error_page')

        except Exception as e:
             return redirect('error_page')
           
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
    return redirect('home') 