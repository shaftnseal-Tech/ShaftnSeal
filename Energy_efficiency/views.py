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
from django.forms.models import model_to_dict





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
            instance = form.save(commit=False)
            instance.user = request.user  # 👈 Assign the logged-in user
            instance.save()
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
def pump_efficiency_calculater(request):
    # Get the latest submission by the user (assuming 'created_at' or use '-id')
    form_data = Energy_Efficiency_Parameters.objects.filter(user_id=request.user.id).order_by('-id').first()
    
    if form_data:
        data = model_to_dict(form_data)
        h1 = data['height1']
        h2 = data['height2']
        p1 = data['suction_pressure']
        p2 = data['discharge_pressure']
        t = data['fluid_temperature']
        text_curve_data = data['text_curve_data']
        philosophy = '1R + 1s'
        Qnp_value = data['nominal_flow_rate']
        Hnp_value = data['nominal_head']
        
        
        
        obj = PumpEfficiency()
        spg = obj.get_specific_gravity(t)
        Static_head = obj.calculate_static_head(h1,h2,p1,p2)
        k1 = obj.calculate_theoretical_src(philosophy,Qnp_value,Hnp_value,text_curve_data)
        Graph_url = obj.display_src()
        media_url_path = Graph_url.replace(settings.MEDIA_ROOT, settings.MEDIA_URL).replace("\\", "/")
        print("Graph_url:",media_url_path)
        print('Static Head:', Static_head)
        print('Specific Gravity',spg)
        print('k1',k1)
        print('',k1)
        
        print(obj.get_specific_gravity(t))
        return render(request, 'Energy_efficiency/Efficiency_calculation.html', {
            'form_data': data,'Graph_url': media_url_path,
        })
    else:
       
        return render(request, 'Energy_efficiency/Efficiency_calculation.html', {
            'error': 'No submissions found for your account.'
        })





@login_required
def finalize_submission(request):
    """Handle the final submission of the draft data."""

    return render(
        request,
        'Energy_efficiency/finalize_submission.html',
      
    )
