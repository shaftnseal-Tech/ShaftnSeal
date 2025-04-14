from django import forms

class System_data(forms.Form):
    h1 = forms.FloatField(widget=forms.NumberInput(attrs={'class':'input-modal' ,'type':'text','placeholder':'Enter Suction Tank Height (m):  '}),label='')
    h2 = forms.FloatField(widget=forms.NumberInput(attrs={'class':'input-modal' ,'type':'text','placeholder':'Enter Discharge Drum Height (m): '}),label='')
    p1 = forms.FloatField(widget=forms.NumberInput(attrs={'class':'input-modal' ,'type':'text','placeholder':'Enter Suction Pressure (bar): '}),label='')
    p2 = forms.FloatField(widget=forms.NumberInput(attrs={'class':'input-modal' ,'type':'text','placeholder':'Enter Discharge Pressure (bar): '}),label='')
    temperature = forms.FloatField(widget=forms.NumberInput(attrs={'class':'input-modal' ,'type':'text','placeholder':'Enter Fluid Temperature (°C): '}),label='')
   




class Pump_name_plate_data(forms.Form):
    Qnp = forms.FloatField(required=True,label='',widget=forms.NumberInput(attrs={
            'class': 'input-modal',
            'placeholder': 'Enter Flow Rate (Qnp) in m3/hr',
            
        })
    )

    Hnp = forms.FloatField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'input-modal',
            'placeholder': 'Enter Head (Hnp) in m3/hr' 
        })
    )

    Pump_Efficiency = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'input-modal',
            'placeholder': 'Enter Pump Efficiency in decimal'
        })
    )

    Pump_speed = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'input-modal',
            'placeholder': 'Enter Pump Speed (RPM) '
        })
    )

class Motor_name_plate_data(forms.Form):
    Voltage = forms.FloatField(required=True)
    Current = forms.FloatField(required=True)
    Power_factor = forms.FloatField(required=True)
    Power = forms.FloatField(required=True)
    Motor_Efficiency = forms.FloatField(required=True)
    
class Commercial_data(forms.Form):
    No_of_hrs_pump_running = forms.FloatField(required=True)
    Cost_of_electricity = forms.FloatField(required=True)
    
class Actual_data(forms.Form):
    total_flow_rate = forms.FloatField(required=True)
    actual_suction_pressure = forms.FloatField(required=True)
    actual_discharge_pressure = forms.FloatField(required=True)
    
class Electrical_parameters(forms.Form):
    actual_Voltage = forms.FloatField(required=True)
    actual_Current = forms.FloatField(required=True)
    actual_Power_factor = forms.FloatField(required=True)
    actual_Power = forms.FloatField(required=True)

class Test_curve_data(forms.Form):
    QH_test_data = forms.FileField(required=True)