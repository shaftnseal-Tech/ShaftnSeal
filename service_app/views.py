from django.shortcuts import render

# Create your views here.
def service_page(request):
    return render(request, 'service_app/service_page.html')