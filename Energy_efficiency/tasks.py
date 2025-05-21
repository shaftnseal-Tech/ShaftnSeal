from celery import shared_task
from Energy_efficiency.utils.pdf_generator import generate_efficiency_report_pdf


@shared_task(bind=True, name="run_pump_efficiency_task")
def run_pump_efficiency_task(self,
                             N1, N2, Qnp, Hnp, test_file,
                             h1, h2, p1, p2, Qact, temp, psp, pdp,
                             pump_philosophy):

    try:
        pdf_path = generate_efficiency_report_pdf(
            N1,
            N2,
            Qnp,
            Hnp,
            test_file,
            h1,
            h2,
            p1,
            p2,
            Qact,
            temp,
            psp,
            pdp,
            pump_philosophy
        )
        return pdf_path

    except Exception as e:
        self.retry(exc=e, countdown=10, max_retries=3)
        raise e
