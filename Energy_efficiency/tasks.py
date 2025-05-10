from celery import shared_task
from Energy_efficiency.utils.services import PumpEfficiency

@shared_task(bind=True, name="run_pump_efficiency_task")
def run_pump_efficiency_task(self, N1, N2, Qnp, Hnp, test_file):
    try:
        QH_curve = PumpEfficiency()
        plot_path = QH_curve.text_curve(N1, N2, Qnp, Hnp, test_file)
        return plot_path
    except Exception as e:
        # Optional: Retry logic or logging
        self.retry(exc=e, countdown=10, max_retries=3)  # optional retry
        raise e
