from Energy_efficiency.utils.services import PumpEfficiency
from celery import shared_task


# energy_efficiency/tasks.py

from celery import shared_task
from Energy_efficiency.utils.services import PumpEfficiency  # correct import based on your structure

@shared_task
def run_pump_efficiency_task(temp, h1, h2, p1, p2, pump_philosophy, Qnp, Hnp, excel_file_path):
    pump  = PumpEfficiency()
    
    pump.get_specific_gravity(temp)
    
    pump.calculate_static_head(h1, h2, p1, p2)
    
    pump.calculate_theoretical_src(pump_philosophy, Qnp, Hnp, excel_file_path)
    
    plot_path = pump.display_src()

    return plot_path
