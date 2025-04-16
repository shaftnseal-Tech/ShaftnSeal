import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils.services import PumpEfficiency  # Ensure this is correctly imported
from django.conf import settings
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Energy_Efficiency_Parameters
from .forms import (
    SystemData, PumpNamePlateData, MotorNamePlateData, 
    ActualPumpData, TestData, ElectricalParameters, ComercialData
)
def boiler_feedpump_1r1s_view(request):
   return render(request, "Energy_efficiency/boiler1r+1spump.html")





def Energy_efficiency_view(request):
    return render(request, 'Energy_efficiency/energy_efficiency.html')

def boiler_feedpump_view(request):
    return render(request, 'Energy_efficiency/boilerfeedpump.html')




@login_required
def boiler_form(request):
    if request.method == 'POST':
        system_form = SystemData(request.POST)
        pump_form = PumpNamePlateData(request.POST)
        motor_form = MotorNamePlateData(request.POST)
        actual_form = ActualPumpData(request.POST)
        test_form = TestData(request.POST, request.FILES)
        electrical_form = ElectricalParameters(request.POST)
        commercial_form = ComercialData(request.POST)

        if all([
            system_form.is_valid(), pump_form.is_valid(), motor_form.is_valid(),
            actual_form.is_valid(), test_form.is_valid(),
            electrical_form.is_valid(), commercial_form.is_valid()
        ]):
            system_form.save()
            pump_form.save()
            motor_form.save()
            actual_form.save()
            test_form.save()
            electrical_form.save()
            commercial_form.save()

            messages.success(request, "Data submitted successfully!")
            return redirect('some_success_page')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        system_form = SystemData()
        pump_form = PumpNamePlateData()
        motor_form = MotorNamePlateData()
        actual_form = ActualPumpData()
        test_form = TestData()
        electrical_form = ElectricalParameters()
        commercial_form = ComercialData()

    return render(request, 'Energy_efficiency/form_page.html', {
        'system_data_form': system_form,
        'pump_nameplate_form': pump_form,
        'motor_nameplate_form': motor_form,
        'actual_pump_data_form': actual_form,
        'test_data_form': test_form,
        'electrical_params_form': electrical_form,
        'commercial_data_form': commercial_form,
    })

@login_required
def finalize_submission(request):
    """Handle the final submission of the draft data."""
    
    return render(request,'Energy_efficiency/finalize_submission.html')