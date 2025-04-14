import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from .forms import (
    System_data,
    Pump_name_plate_data,
    Motor_name_plate_data,
    Electrical_parameters,
    Commercial_data,
    Actual_data,
    Test_curve_data,
)
from .utils.services import PumpEfficiency  # Ensure this is correctly imported
from django.conf import settings
import os

def boiler_feedpump_1r1s_view(request):
    graph_url = None
    pdf_url = None  # Variable for the PDF URL

    if request.method == "POST":
        form1 = System_data(request.POST)
        form2 = Pump_name_plate_data(request.POST)
        form3 = Motor_name_plate_data(request.POST)
        form4 = Electrical_parameters(request.POST)
        form5 = Commercial_data(request.POST)
        form6 = Actual_data(request.POST)
        form7 = Test_curve_data(request.POST, request.FILES)

        if (
            form1.is_valid() and form2.is_valid() and form3.is_valid()
            and form4.is_valid() and form5.is_valid() and form6.is_valid()
            and form7.is_valid()
        ):
            # Extract form data
            h1 = form1.cleaned_data['h1']
            h2 = form1.cleaned_data['h2']
            p1 = form1.cleaned_data['p1']
            p2 = form1.cleaned_data['p2']
            temperature = form1.cleaned_data['temperature']

            Qnp = form2.cleaned_data['Qnp']
            Hnp = form2.cleaned_data['Hnp']

            total_flow_rate = form6.cleaned_data['total_flow_rate']
            actual_suction_pressure = form6.cleaned_data['actual_suction_pressure']
            actual_discharge_pressure = form6.cleaned_data['actual_discharge_pressure']

            
            QH_values = form7.cleaned_data['QH_test_data']
           
            obj = PumpEfficiency()
            sepecificgravity = obj.get_specific_gravity(temperature)
            static_head = obj.calculate_static_head(h1, h2, p1, p2)
            k1 = obj.calculate_theoretical_src('2r+1s', Qnp, Hnp, QH_values)
            graph_url = obj.display_src()  
            
            pdf_url = os.path.join(settings.MEDIA_URL, 'src_plot_standard.pdf' if obj.pump_philosophy != '2R + 1s' else 'src_plot_2r1s.pdf')
            print( pdf_url)

    else:
        form1 = System_data()
        form2 = Pump_name_plate_data()
        form3 = Motor_name_plate_data()
        form4 = Electrical_parameters()
        form5 = Commercial_data()
        form6 = Actual_data()
        form7 = Test_curve_data()

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        'form6': form6,
        'form7': form7,
        'graph_url': graph_url,
        'pdf_url': pdf_url,  # Pass the PDF URL to the template
    }

    return render(request, "Energy_efficiency/boiler1r+1spump.html", context)





def Energy_efficiency_view(request):
    return render(request, 'Energy_efficiency/energy_efficiency.html')

def boiler_feedpump_view(request):
    return render(request, 'Energy_efficiency/boilerfeedpump.html')


