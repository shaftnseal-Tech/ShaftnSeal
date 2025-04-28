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
from django.views.decorators.cache import cache_page

from .tasks import run_pump_efficiency_task
import os
import matplotlib.pyplot as plt





def boiler_feedpump_1r1s_view(request):
    pump_name = request.GET.get('pump_name')
    if pump_name:
        request.session['pump_name'] = str(pump_name)
    print(pump_name)
    return render(request, "Energy_efficiency/boiler1r+1spump.html")


def boiler_feedpump_2r1s_view(request):
    pump_name = request.GET.get('pump_name')
    if pump_name:
        request.session['pump_name'] = str(pump_name)
    print(pump_name)
    return render(request, "Energy_efficiency/boiler2r+1spump.html")



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
  # import your celery task
from .tasks import run_pump_efficiency_task


@login_required
def pump_efficiency_calculater(request):
    # Get the latest submission by the user (assuming 'created_at' or use '-id')
    form_data = Energy_Efficiency_Parameters.objects.filter(user_id=request.user.id).order_by('-id').first()
    pump_name = request.session.get('pump_name', 'No pump selected')

    if form_data:
        data = model_to_dict(form_data)
        
        # Extract necessary values from form data
        temp = data['fluid_temperature']
        h1 = data['height1']
        h2 = data['height2']
        p1 = data['suction_pressure']
        p2 = data['discharge_pressure']
        pump_philosophy = pump_name
        Qnp = data['nominal_flow_rate']
        Hnp = data['nominal_head']
        
        # Handle the file path for 'text_curve_data' (if it exists)
        excel_file = data.get('text_curve_data', None)
        excel_file_path = None
        if excel_file:
            # If it's a FieldFile, get the actual file path
            excel_file_path = excel_file.path
            print(f"Excel file path: {excel_file_path}")
        
        # Call the Celery task with the necessary arguments
        result = run_pump_efficiency_task.apply_async(
            args=[temp, h1, h2, p1, p2, pump_philosophy, Qnp, Hnp, excel_file_path]
        )

        # If you want to wait for the result synchronously (blocking)
        try:
            plot_path = result.get(timeout=300)  # Set timeout in case of issues
            
            # Handle the plot URL generation and media path correction
            if plot_path:
                media_url_path = plot_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL).replace("\\", "/")
                return render(request, 'Energy_efficiency/Efficiency_calculation.html', {
                    'form_data': data,
                    'Graph_url': media_url_path,
                })
            else:
                messages.error(request, "Failed to generate graph.")
                return redirect('pump_efficiency_calculater')
        except Exception as e:
            # Handle task failure or timeout
            messages.error(request, f"Error occurred while processing: {str(e)}")
            return redirect('pump_efficiency_calculater')
    else:
        messages.error(request, "No submissions found for your account.")
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
