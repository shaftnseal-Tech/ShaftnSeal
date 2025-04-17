import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils.services import PumpEfficiency 
from django.conf import settings
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Energy_Efficiency_Parameters
from .forms import EnergyEfficiencyForm





def boiler_feedpump_1r1s_view(request):
   return render(request, "Energy_efficiency/boiler1r+1spump.html")


def Energy_efficiency_view(request):
    return render(request, 'Energy_efficiency/energy_efficiency.html')


def boiler_feedpump_view(request):
    return render(request, 'Energy_efficiency/boilerfeedpump.html')


@login_required
def boiler_form(request):
    if request.method == 'POST':
        form = EnergyEfficiencyForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Data submitted successfully!")
            return redirect('final_submission') 
        else:
         
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = EnergyEfficiencyForm()

    return render(request, 'Energy_efficiency/form_page.html', {
        'form': form,
    })

@login_required
def finalize_submission(request):
    """Handle the final submission of the draft data."""
    
    return render(request,'Energy_efficiency/finalize_submission.html')