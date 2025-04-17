from django import forms
from .models import Energy_Efficiency_Parameters

class EnergyEfficiencyForm(forms.ModelForm):
    class Meta:
        model = Energy_Efficiency_Parameters
        fields = [
            # System Data Fields
            'height1', 'height2', 'suction_pressure', 'discharge_pressure', 'fluid_temperature',
            # Pump Name Plate Fields
            'nominal_flow_rate', 'nominal_head', 'pump_efficiency', 'pump_speed',
            # Motor Name Plate Fields
            'motor_voltage', 'motor_power_factor', 'motor_power', 'N1',
            # Actual Pump Data Fields
            'actual_flow_rate', 'pump_discharge_pressure', 'pump_suction_pressure',
            # Test Data Fields
            'text_curve_data',
            # Electrical Parameters Fields
            'actual_voltage', 'actual_power_factor', 'actual_power', 'actual_efficiency', 'N2',
            # Commercial Data Fields
            'no_hrs_pumprun', 'cost_of_electricity'
        ]
        
        labels = {
            'height1': 'Height between Suction tank and center of the pump (h1)',
            'height2': 'Height between Discharge tank and center of the pump (h2)',
            'suction_pressure': 'Suction tank pressure (kg/cm²)',
            'discharge_pressure': 'Discharge tank pressure (kg/cm²)',
            'fluid_temperature': 'Fluid Temperature (°C)',
            
            'nominal_flow_rate': 'Pump name plate flow (m³/hr)',
            'nominal_head': 'Pump name plate head (m)',
            'pump_efficiency': 'Pump Efficiency (%)',
            'pump_speed': 'Pump speed (rpm)',
            
            'motor_voltage': 'Motor Voltage (volts)',
            'motor_power_factor': 'Motor Power Factor (pf)',
            'motor_power': 'Motor Power output (kWh)',
            'N1': 'Speed (N1) in (rpm)',
           
            'actual_flow_rate': 'Total Flow Rate in 24hrs (m³/hr)',
            'pump_discharge_pressure': 'Pump Discharge Pressure (kg/cm²)',
            'pump_suction_pressure': 'Pump Suction Pressure (kg/cm²)',
            
            'text_curve_data': 'Upload Test Data',
           
            'actual_voltage': 'Actual Voltage (volts)',
            'actual_power_factor': 'Actual Power Factor (pf)',
            'actual_power': 'Actual Power (kWh)',
            'actual_efficiency': 'Actual Efficiency (%)',
            'N2': 'Actual Speed (N2) in (rpm)',
           
            'no_hrs_pumprun': 'Number of hours pump in operation per year',
            'cost_of_electricity': 'Cost of Electricity per kWh'
        }

        widgets = {
           
            'height1': forms.NumberInput(attrs={'class': 'form-control'}),
            'height2': forms.NumberInput(attrs={'class': 'form-control'}),
            'suction_pressure': forms.NumberInput(attrs={'class': 'form-control'}),
            'discharge_pressure': forms.NumberInput(attrs={'class': 'form-control'}),
            'fluid_temperature': forms.NumberInput(attrs={'class': 'form-control'}),

            'nominal_flow_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'nominal_head': forms.NumberInput(attrs={'class': 'form-control'}),
            'pump_efficiency': forms.NumberInput(attrs={'class': 'form-control'}),
            'pump_speed': forms.NumberInput(attrs={'class': 'form-control'}),

            'motor_voltage': forms.NumberInput(attrs={'class': 'form-control'}),
            'motor_power_factor': forms.NumberInput(attrs={'class': 'form-control'}),
            'motor_power': forms.NumberInput(attrs={'class': 'form-control'}),
            'N1': forms.NumberInput(attrs={'class': 'form-control'}),

         
            'actual_flow_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'pump_discharge_pressure': forms.NumberInput(attrs={'class': 'form-control'}),
            'pump_suction_pressure': forms.NumberInput(attrs={'class': 'form-control'}),

            'text_curve_data': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.csv,.txt,.xlsx',
            }),

    
            'actual_voltage': forms.NumberInput(attrs={'class': 'form-control'}),
            'actual_power_factor': forms.NumberInput(attrs={'class': 'form-control'}),
            'actual_power': forms.NumberInput(attrs={'class': 'form-control'}),
            'actual_efficiency': forms.NumberInput(attrs={'class': 'form-control'}),
            'N2': forms.NumberInput(attrs={'class': 'form-control'}),

           
            'no_hrs_pumprun': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_of_electricity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
