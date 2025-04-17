from django.db import models
from accounts.models import Account

class Energy_Efficiency_Parameters(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Basic input parameters
    height1 = models.FloatField(verbose_name='Height1')
    height2 = models.FloatField(verbose_name='Height2')
    suction_pressure = models.FloatField(verbose_name='Suction Pressure')
    discharge_pressure = models.FloatField(verbose_name='Discharge Pressure')
    fluid_temperature = models.FloatField(verbose_name='Fluid Temperature')

    nominal_flow_rate = models.FloatField(verbose_name='Qnp')
    nominal_head = models.FloatField(verbose_name='Hnp')
    pump_efficiency = models.FloatField(verbose_name='Pump Efficiency')
    pump_speed = models.FloatField(verbose_name='Pump Speed')

    motor_voltage = models.FloatField(verbose_name='Motor Voltage')
    motor_current = models.FloatField(verbose_name='Motor Current')
    motor_power_factor = models.FloatField(verbose_name='Motor Power Factor')
    motor_power = models.FloatField(verbose_name='Power')

    N1 = models.FloatField(verbose_name='N1')
    N2 = models.FloatField(verbose_name='N2')

    actual_flow_rate = models.FloatField(verbose_name='Actual Flow Rate')
    pump_discharge_pressure = models.FloatField(verbose_name='Pump Discharge Pressure')
    pump_suction_pressure = models.FloatField(verbose_name='Pump Suction Pressure')

    text_curve_data = models.FileField(verbose_name='Test Data', upload_to='test_curve_data/')

    actual_voltage = models.FloatField(verbose_name='Actual Voltage')
    actual_current = models.FloatField(verbose_name='Actual Vlotage')
    actual_power_factor = models.FloatField(verbose_name='Actual Power Factor')
    actual_power = models.FloatField(verbose_name='Actual Power')
    actual_efficiency = models.FloatField(verbose_name='Actual Efficiency')

    no_hrs_pumprun = models.FloatField(verbose_name='No. of Hours Pump Run')
    cost_of_electricity = models.FloatField(verbose_name='Cost of Electricity')

   

    class Meta:
        db_table = 'Energy_Efficiency_Parameters'  
        verbose_name = "Energy Efficiency Parameter" 
        verbose_name_plural = "Energy Efficiency Parameters"

 
