from django import forms
from .models import Energy_Efficiency_Parameters

class SystemData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'height1', 'height2', 'suction_pressure', 'discharge_pressure', 
            'fluid_temperature',
        ]
        labels = {
            'height1':' Height between Suction tank and center of the pump (h1)',
            'height2':' Height between Discharge tank and center of the pump (h2)',
            'suction_pressure':'Suction tank pressure  (kg/cm²)',
            'discharge_pressure':'Discharge tank pressure  (kg/cm²)',
            'fluid_temperature':'Fluid Temperature  (DC)',
            
        }

class PumpNamePlateData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'nominal_flow_rate', 'nominal_head', 'pump_efficiency', 'pump_speed',
        ]
        labels ={
            'nominal_flow_rate':'Pump name plate flow  (m³/hr)',
            'nominal_head':'Pump name plate head  (m)',
            'pump_efficiency':'Pump Efficiency  (%)',
            'pump_speed':'Pump speed (rpm)'
        }
        
class MotorNamePlateData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'motor_voltage', 'motor_power_factor', 'motor_power', 'N1', 
        ]
        labels = {
            'motor_voltage':'Motor Voltage (volts)',
            'motor_power_factor':'Motor Power Facter(pf)',
            'motor_power': 'Motor Power output(kwh)',
            'N1':'Speed(N1) in(rpm)'
            
        }

class ActualPumpData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'actual_flow_rate', 'pump_discharge_pressure', 'pump_suction_pressure'
        ]
        labels ={
            'actual_flow_rate':'Total Flow Rate in 24hrs (m³/hr)',
            'pump_suction_pressure':'Pump Suction Pressure (kg/cm²)',
            'pump_discharge_pressure':'Pump Discharge Pressure (kg/cm²)',
        }

class TestData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'text_curve_data'
        ]
        labels = {
            'text_curve_data':'Upload Test Data'
        }
class ElectricalParameters(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'actual_voltage', 'actual_power_factor', 'actual_power', 'actual_efficiency','N2',
        ]
        labels={
            'actual_voltage':'Actual Voltage (volts)',
            'actual_power_factor':'Actual Power Factor (pf)',
            'actual_power':'Actual power (kwh)',
            'actual_efficiency':'Actual Efficiency (%)',
            'N2':'Actual speed (rpm)'
        }
class ComercialData(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            'no_hrs_pumprun', 'cost_of_electricity'
        ]
        labels = {
            'no_hrs_pumprun':'Number of hrs pump in operation per year',
            'cost_of_electricity':'Cost of Electricity per kwh'
        }