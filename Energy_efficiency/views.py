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





# Util: Get or create a draft instance
def get_draft_only(request):
    if not request.user.is_authenticated:
        return None
    draft = Energy_Efficiency_Parameters.objects.filter(user=request.user, is_draft=True).first()
    if not draft:
        draft = Energy_Efficiency_Parameters.objects.create(user=request.user, is_draft=True)
    return draft

@login_required
def boiler_form(request):
    

    draft = get_draft_only(request)

    if request.method == 'POST':
        # All forms and their corresponding trigger buttons
        form_data = [
            ('save_system_data', SystemData, 'System Data'),
            ('save_pump_nameplate', PumpNamePlateData, 'Pump Nameplate Data'),
            ('save_motor_nameplate', MotorNamePlateData, 'Motor Nameplate Data'),
            ('save_actual_pump_data', ActualPumpData, 'Actual Pump Data'),
            ('save_test_data', TestData, 'Test Data'),
            ('save_electrical_params', ElectricalParameters, 'Electrical Parameters'),
            ('save_commercial_data', ComercialData, 'Commercial Data'),
        ]

        # Identify which form was submitted
        for action, form_class, form_name in form_data:
            if action in request.POST:
                form = form_class(request.POST, request.FILES, instance=draft)

                if form.is_valid():
                    form.save()
                    messages.success(request, f"{form_name} saved successfully.")

                    if form_name == 'Commercial Data':
                        return redirect('final_submission')
                    return redirect('form-page')

                messages.error(request, f"Failed to save {form_name}. Please check the form for errors.")

    else:
        # On GET, load all forms with the current draft instance
        system_data_form = SystemData(instance=draft)
        pump_nameplate_form = PumpNamePlateData(instance=draft)
        motor_nameplate_form = MotorNamePlateData(instance=draft)
        actual_pump_data_form = ActualPumpData(instance=draft)
        test_data_form = TestData(instance=draft)
        electrical_params_form = ElectricalParameters(instance=draft)
        commercial_data_form = ComercialData(instance=draft)

    return render(request, 'Energy_efficiency/form_page.html', {
        'system_data_form': system_data_form,
        'pump_nameplate_form': pump_nameplate_form,
        'motor_nameplate_form': motor_nameplate_form,
        'actual_pump_data_form': actual_pump_data_form,
        'test_data_form': test_data_form,
        'electrical_params_form': electrical_params_form,
        'commercial_data_form': commercial_data_form,
    })

@login_required
def finalize_submission(request):
    """Handle the final submission of the draft data."""
    
    draft = get_draft_only(request)

    if draft:
        draft.is_draft = False  # Mark the draft as finalized
        draft.save()

    return render(request,'Energy_efficiency/finalize_submission.html')