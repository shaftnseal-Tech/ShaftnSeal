import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from django.shortcuts import render
from .forms import PumpAnalysisForm

def pump_analysis_view(request):
    graph_url = None  # Placeholder for graph image
    
    if request.method == "POST":
        form = PumpAnalysisForm(request.POST)
        
        if form.is_valid():
            # Get form data
            h1 = form.cleaned_data['h1']
            h2 = form.cleaned_data['h2']
            p1 = form.cleaned_data['p1']
            p2 = form.cleaned_data['p2']
            temperature = form.cleaned_data['temperature']
            specific_gravity = form.cleaned_data['specific_gravity']
            Q_act = form.cleaned_data['Q_act']
            H_act = form.cleaned_data['H_act']
            Qnp = form.cleaned_data['Qnp']
            Hnp = form.cleaned_data['Hnp']

            # Calculate Static Head
            static_head = h2 - h1

            # Convert pressures from bar to meters of liquid column
            pressure_head = ((p2 - p1) * 10) / specific_gravity  # 1 bar ≈ 10 meters water column

            # Calculate Dynamic Head
            dynamic_head = H_act - static_head - pressure_head

            # Compute SRC using the constant K
            k = dynamic_head / (Q_act ** 2)
            Q_values = np.linspace(0, Qnp * 1.2, 50)  # Generate flow rates
            SRC_values = static_head + pressure_head + k * (Q_values ** 2)

            # Compute Theoretical Pump Curve
            H_theoretical = Hnp * (1 - (Q_values / Qnp) ** 2)

            # Plot graph
            plt.figure(figsize=(7, 5))
            plt.plot(Q_values, H_theoretical, 'b--', label="Theoretical Pump Curve")
            plt.plot(Q_values, SRC_values, 'r-', label="System Resistance Curve (SRC)")
            plt.scatter(Q_act, H_act, color='green', label="Actual Operating Point")
            plt.xlabel("Flow Rate (Q) in m³/h")
            plt.ylabel("Head (H) in meters")
            plt.title("Comparison of Theoretical and Actual SRC Curves")
            plt.legend()
            plt.grid(True)

            # Convert plot to image
            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            graph_url = base64.b64encode(buf.getvalue()).decode("utf-8")
            buf.close()
    
    else:
        form = PumpAnalysisForm()
    
    return render(request, "Energy_efficiency/src_graph.html", {"form": form, "graph_url": graph_url})
