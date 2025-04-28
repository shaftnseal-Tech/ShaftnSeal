from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(60 * 15) 
def service_page(request):
    return render(request, 'service_app/service_page.html')