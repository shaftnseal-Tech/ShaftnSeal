from django import forms

class PumpAnalysisForm(forms.Form):
    h1 = forms.FloatField(label="Suction Tank Height (m)")
    h2 = forms.FloatField(label="Discharge Drum Height (m)")
    p1 = forms.FloatField(label="Suction Pressure (bar)")
    p2 = forms.FloatField(label="Discharge Pressure (bar)")
    temperature = forms.FloatField(label="Fluid Temperature (°C)")
    specific_gravity = forms.FloatField(label="Specific Gravity of Fluid")
    Q_act = forms.FloatField(label="Actual Flow Rate (m³/h)")
    H_act = forms.FloatField(label="Actual Head (m)")
    Qnp = forms.FloatField(label="Nominal Flow Rate (m³/h)")
    Hnp = forms.FloatField(label="Nominal Head (m)")
