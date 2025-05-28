from django.shortcuts import render



def pump_page(request):
    return render(request, 'pump/pump.html')


def error_page(request):
    return render(request, 'pump/error_page.html')

def new_pump(request):
    return render(request, 'pump/newpump.html')
